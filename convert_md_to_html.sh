#!/bin/bash
# Convert index.md to index.html
# Produces output styled like VS Code's markdown preview using CDN stylesheets

set -e

MD_FILE="${1:-index.md}"
HTML_FILE="${2:-index.html}"

if [ ! -f "$MD_FILE" ]; then
    echo "Error: $MD_FILE not found"
    exit 1
fi

echo "Converting $MD_FILE to $HTML_FILE..."

# Split the file: HTML section (before first ##) and Markdown section (from ## onward)
HTML_SECTION=$(mktemp)
MD_SECTION=$(mktemp)
sed '/^## /,$d' "$MD_FILE" > "$HTML_SECTION"
sed -n '/^## /,$p' "$MD_FILE" > "$MD_SECTION"

echo "  HTML section: $(wc -l < "$HTML_SECTION") lines"
echo "  Markdown section: $(wc -l < "$MD_SECTION") lines"

# Convert only the markdown section to HTML
MD_HTML=$(mktemp)
pandoc "$MD_SECTION" \
    -f markdown-fancy_lists \
    -t html \
    --tab-stop=2 \
    -o "$MD_HTML"

# Assemble the full HTML document
cat > "$HTML_FILE" <<'HEADER'
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Research and Software Projects</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/markdown.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/highlight.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
    <link rel="stylesheet" href="./styles.css">
</head>
<body class="vscode-body vscode-light">
    <div class="markdown-body github-markdown-body" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark">
        <div class="github-markdown-content">
HEADER

# Append the HTML section (preserved as-is) and converted markdown
cat "$HTML_SECTION" >> "$HTML_FILE"
cat "$MD_HTML" >> "$HTML_FILE"

cat >> "$HTML_FILE" <<'FOOTER'
        </div>
    </div>
</body>
</html>
FOOTER

# Cleanup
rm -f "$HTML_SECTION" "$MD_SECTION" "$MD_HTML"

echo "✅ Created $HTML_FILE ($(wc -l < "$HTML_FILE") lines, $(ls -lh "$HTML_FILE" | awk '{print $5}'))"
echo ""
echo "  open $HTML_FILE"
echo "  git diff $HTML_FILE"
