#!/bin/bash
# ─────────────────────────────────────────────
# Socialbrand 1980 — Photo MCP Install Script
# ─────────────────────────────────────────────

echo "📦 Installing dependencies..."
pip3 install -r "$(dirname "$0")/requirements.txt"

echo ""
echo "✅ Done! Add this to your Claude Code config (claude_desktop_config.json):"
echo ""
echo '{'
echo '  "mcpServers": {'
echo '    "socialbrand-photo": {'
echo '      "command": "python3",'
echo '      "args": ["'$(cd "$(dirname "$0")" && pwd)'/server.py"]'
echo '    }'
echo '  }'
echo '}'
echo ""
echo "📍 MCP path: $(cd "$(dirname "$0")" && pwd)/server.py"
