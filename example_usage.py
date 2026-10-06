"""Example usage for Ad Copy Hook & CTA Synthesizer."""
from client import AdCopyHookCTASynthesizer

if __name__ == "__main__":
    pkg = AdCopyHookCTASynthesizer.generate_ad_package(
        "GenPark Edge Engine",
        "Autonomous edge agent orchestration",
        "AI Founders & SREs"
    )
    print("Product:", pkg["product"])
    for h in pkg["hooks"]:
        print(f"[{h['framework']}] {h['hook_text']}")
