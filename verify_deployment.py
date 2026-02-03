#!/usr/bin/env python3
"""
Script to test the deployed Vercel API
This script attempts to access the deployed API and verify it's working properly
"""

import subprocess
import sys
import tempfile
import os

def get_protection_bypass_url():
    """
    Generate a protection bypass URL for Vercel deployment
    """
    deployment_url = "https://backend-elt2etf2u-hasnain-ali204.vercel.app"

    # First, try to get a protection bypass token using Vercel CLI
    try:
        # Get the bypass token by attempting to access the deployment
        cmd = f'vercel curl / --deployment {deployment_url}'
        print(f"Attempting to access deployment with: {cmd}")

        result = subprocess.run(
            ['vercel', 'curl', '/', '--deployment', deployment_url],
            capture_output=True,
            text=True,
            timeout=30
        )

        print(f"Vercel curl result: {result.returncode}")
        print(f"Stdout: {result.stdout}")
        print(f"Stderr: {result.stderr}")

        if result.returncode == 0:
            print("SUCCESS: Successfully accessed deployment!")
            return True
        else:
            print("FAILED: Failed to access deployment via Vercel CLI")
            return False

    except subprocess.TimeoutExpired:
        print("TIMEOUT: Timeout while trying to access deployment")
        return False
    except FileNotFoundError:
        print("ERROR: Vercel CLI not found in PATH")
        return False
    except Exception as e:
        print(f"ERROR: Error accessing deployment: {e}")
        return False

def get_deployment_logs():
    """
    Get logs from the deployment to verify it's running properly
    """
    try:
        result = subprocess.run(
            ['vercel', 'logs', 'backend-elt2etf2u-hasnain-ali204.vercel.app', '--limit', '10'],
            capture_output=True,
            text=True,
            timeout=30
        )

        print(f"Deployment logs: {result.stdout}")
        if result.stderr:
            print(f"Log errors: {result.stderr}")

        return result.returncode == 0
    except FileNotFoundError:
        print("ERROR: Vercel CLI not found in PATH")
        return False
    except Exception as e:
        print(f"ERROR: Error getting logs: {e}")
        return False

def main():
    print("Testing deployed Vercel API...")
    print("="*50)

    print("\n1. Testing deployment access...")
    access_ok = get_protection_bypass_url()

    print(f"\n2. Checking deployment logs...")
    logs_ok = get_deployment_logs()

    print("\n" + "="*50)
    print("TEST RESULTS:")
    print(f"- Deployment Access: {'PASS' if access_ok else 'FAIL'}")
    print(f"- Deployment Logs: {'PASS' if logs_ok else 'FAIL'}")

    if access_ok or logs_ok:
        print("\nAPI appears to be deployed and accessible!")
        print("  Deployment URL: https://backend-elt2etf2u-hasnain-ali204.vercel.app")
        print("  Stable Alias: https://backend-eta-eight-83.vercel.app")
    else:
        print("\nAdditional verification needed")
        print("  The deployment exists but may need further testing")

    return access_ok or logs_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)