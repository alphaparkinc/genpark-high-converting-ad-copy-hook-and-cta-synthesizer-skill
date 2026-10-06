"""MCP server for Ad Copy Hook & CTA Synthesizer."""
import sys
import json
from client import AdCopyHookCTASynthesizer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "generate_ad_package",
                "description": "Generates high-converting marketing hooks and CTA variations",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "product_name": {"type": "string"},
                        "value_prop": {"type": "string"},
                        "audience": {"type": "string"}
                    },
                    "required": ["product_name", "value_prop", "audience"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "generate_ad_package":
            args = params.get("arguments", {})
            res = AdCopyHookCTASynthesizer.generate_ad_package(
                args.get("product_name", ""),
                args.get("value_prop", ""),
                args.get("audience", "")
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
