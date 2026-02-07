#!/bin/bash
# Convert index.md to index.html
# Handles the mixed HTML/Markdown format correctly

set -e

MD_FILE="${1:-index.md}"
HTML_FILE="${2:-index.html}"
TEMP_MD="/tmp/index_processed.md"

if [ ! -f "$MD_FILE" ]; then
    echo "Error: $MD_FILE not found"
    exit 1
fi

echo "Converting $MD_FILE to $HTML_FILE..."

# Pre-process the markdown to prevent HTML from being treated as code blocks
# The issue is that indented HTML (with tabs) gets treated as a code block by pandoc
# We need to un-indent the HTML section at the top

# Split the file at the first ## header (where markdown starts)
awk '
/^## / { markdown=1 }
!markdown {
    # Remove leading tabs from HTML section to prevent code block treatment
    gsub(/^\t+/, "")
    print
}
markdown { print }
' "$MD_FILE" > "$TEMP_MD"

echo "Pre-processed markdown to handle HTML sections..."

# Convert using pandoc with settings for GFM-style markdown
# Don't use --embed-resources so images stay as external references
pandoc "$TEMP_MD" \
    -f markdown \
    -t html5 \
    --standalone \
    -c ./styles.css \
    --metadata title="Research and Software Projects" \
    -o "$HTML_FILE"

# Clean up
rm -f "$TEMP_MD"

if [ -f "$HTML_FILE" ]; then
    echo "✅ Successfully created $HTML_FILE ($(wc -l < "$HTML_FILE") lines)"

    echo ""
    echo "Checking image links..."
    if grep -q 'img src=.*anderson_headshot' "$HTML_FILE"; then
        IMG_SRC=$(grep -o 'img src="[^"]*anderson_headshot[^"]*"' "$HTML_FILE" | head -1)
        echo "  Found: <$IMG_SRC>"
    fi

    echo ""
    echo "To compare with previous version:"
    echo "  git diff --stat $HTML_FILE"
    echo "  git diff $HTML_FILE | head -50"
else
    echo "❌ Failed to create $HTML_FILE"
    exit 1
fi
