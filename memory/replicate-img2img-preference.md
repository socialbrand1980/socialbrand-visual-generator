---
name: Replicate Img2Img Preference
description: Prefer Replicate API for img2img campaign photo generation (free $20 credit, ~1000+ images)
type: project
---

**Decision:** Use Replicate API for AI image generation instead of fal.ai

**Why:** fal.ai API key exhausted (no saldo). Replicate offers:
- Free $20 credit on signup (~1000+ campaign images)
- Pay-per-use after (~$0.02-0.10 per image)
- Full img2img support with FLUX.1 Pro/Dev
- Can transform product photos while maintaining product integrity
- Strength control (0.6-0.7) to balance original vs new elements

**How to apply:** 
- When generating campaign/product photos, use Replicate MCP server
- Workflow: raw product photo + moodboard reference → img2img transform → campaign visual
- Ideal for 2bShine and future brand campaigns
- API token stored in `mcp/.env` as `REPLICATE_API_TOKEN`

**Setup required:**
1. User signs up at replicate.com (free)
2. Get API token from dashboard
3. Add to mcp/.env
4. Create/modify MCP server to use Replicate instead of fal.ai
