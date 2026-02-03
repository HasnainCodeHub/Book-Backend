import requests
import os
import subprocess
import json

def get_deployment_protection_bypass():
    """Get deployment protection bypass token using Vercel CLI"""
    try:
        # Get the current project
        result = subprocess.run(['vercel', 'link'], capture_output=True, text=True, cwd=os.getcwd())

        # Get deployment info
        result = subprocess.run(['vercel', 'inspect', 'backend-elt2etf2u-hasnain-ali204.vercel.app', '--json'],
                               capture_output=True, text=True, cwd=os.getcwd())

        if result.returncode == 0:
            deployment_info = json.loads(result.stdout)
            print(f"Deployment info: {deployment_info}")

        # Try to get bypass token
        result = subprocess.run(['vercel', 'env', 'ls', '--environment', 'production', '--json'],
                               capture_output=True, text=True, cwd=os.getcwd())
        print(f"Env result: {result.stdout}, stderr: {result.stderr}")

        return True
    except Exception as e:
        print(f"Error getting deployment info: {e}")
        return False

def test_api_endpoints():
    """Test the deployed API endpoints"""
    base_url = "https://backend-elt2etf2u-hasnain-ali204.vercel.app"

    # Common endpoints to test
    endpoints = [
        "/",
        "/docs",
        "/redoc",
        "/openapi.json",
        "/api/health"  # assuming a health check endpoint exists
    ]

    headers = {
        'User-Agent': 'Vercel-CLI-Test',
        'Accept': 'application/json'
    }

    for endpoint in endpoints:
        try:
            print(f"\nTesting {base_url}{endpoint}")
            response = requests.get(f"{base_url}{endpoint}", headers=headers, timeout=10)
            print(f"Status: {response.status_code}")
            print(f"Headers: {dict(response.headers)}")

            # Try to get content preview
            content_preview = response.text[:200] if len(response.text) > 200 else response.text
            print(f"Content preview: {content_preview}...")

        except requests.exceptions.RequestException as e:
            print(f"Error accessing {endpoint}: {e}")

if __name__ == "__main__":
    print("Testing deployed API...")
    get_deployment_protection_bypass()
    test_api_endpoints()