#!/usr/bin/env python3
"""
Convert index.md to index.html, matching the existing structure.
The existing index.html has embedded VSCode CSS/JS, but we'll create
a cleaner version that matches the content structure.
"""
import re
import subprocess
import sys

def read_file(filepath):
    """Read file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def convert_markdown_to_html(md_content):
    """
    Convert markdown to HTML using Python's markdown library.
    If not available, falls back to a simple converter.
    """
    try:
        import markdown
        # Convert markdown with extra extensions for better compatibility
        html = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        return html
    except ImportError:
        print("Warning: markdown library not found. Install with: pip install markdown", file=sys.stderr)
        print("Falling back to simple conversion...", file=sys.stderr)
        # Simple fallback converter
        lines = md_content.split('\n')
        html_lines = []
        in_list = False

        for line in lines:
            stripped = line.strip()

            # Handle headers
            if stripped.startswith('## '):
                html_lines.append(f'<h2 id="{stripped[3:].lower().replace(" ", "-")}">{stripped[3:]}</h2>')
            elif stripped.startswith('# '):
                html_lines.append(f'<h1>{stripped[2:]}</h1>')
            # Handle list items
            elif stripped.startswith('- '):
                if not in_list:
                    html_lines.append('<ul>')
                    in_list = True
                # Convert markdown links to HTML
                item = stripped[2:]
                item = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', item)
                item = re.sub(r'`([^`]+)`', r'<code>\1</code>', item)
                html_lines.append(f'<li>{item}</li>')
            else:
                if in_list and stripped:
                    in_list = False
                    html_lines.append('</ul>')
                if stripped:
                    html_lines.append(line)
                elif html_lines:  # preserve blank lines
                    html_lines.append('')

        if in_list:
            html_lines.append('</ul>')

        return '\n'.join(html_lines)

def process_index_md(md_path, html_path):
    """
    Convert index.md to index.html.
    The md file has HTML at the top and markdown below.
    """
    content = read_file(md_path)

    # Split content - HTML section is everything before "## Research"
    # Find where markdown starts (first ## header)
    match = re.search(r'^## ', content, re.MULTILINE)

    if match:
        html_section = content[:match.start()].rstrip()
        md_section = content[match.start():].rstrip()
    else:
        # If no markdown section found, treat all as HTML
        html_section = content
        md_section = ""

    # Convert markdown section to HTML
    if md_section:
        md_html = convert_markdown_to_html(md_section)
    else:
        md_html = ""

    # Build the complete HTML
    # Match the structure of the existing HTML file
    html_content = f"""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Research and Software Projects</title>
            <style>
/* From extension vscode.github */
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.vscode-dark img[src$=\\#gh-light-mode-only],
.vscode-light img[src$=\\#gh-dark-mode-only],
.vscode-high-contrast:not(.vscode-high-contrast-light) img[src$=\\#gh-light-mode-only],
.vscode-high-contrast-light img[src$=\\#gh-dark-mode-only] {{
\tdisplay: none;
}}

/* Add any additional styles here */
            </style>
        </head>
        <body>
            <div class="vscode-body">
                <div class="markdown-body">
                    <div class="github-markdown-body">
                        <div class="github-markdown-content">
                            <span class="code-line"
                    data-line-num="1"
                    data-source-path="index.md"
                    data-dark-mode-theme="default"
                    data-light-mode-theme="default"
                    data-max-text-size="50000"></span>
                {html_section}
{md_html}
</div>
        </div>

        </body>
        </html>
"""

    write_file(html_path, html_content)
    print(f"✓ Converted {md_path} to {html_path}")

def main():
    md_path = 'index.md'
    html_path = 'index.html'

    # Back up the existing HTML
    backup_path = 'index.html.backup'
    try:
        subprocess.run(['cp', html_path, backup_path], check=True)
        print(f"✓ Backed up {html_path} to {backup_path}")
    except subprocess.CalledProcessError:
        print(f"Warning: Could not create backup", file=sys.stderr)

    # Convert
    process_index_md(md_path, html_path)

    # Show git diff
    print("\n" + "="*60)
    print("Running git diff to compare...")
    print("="*60 + "\n")
    subprocess.run(['git', 'diff', html_path])

if __name__ == '__main__':
    main()
