"""
Test script to verify PDF processing dependencies work
Run this locally before deploying to make sure everything works
"""

def test_pdf_dependencies():
    print("🔍 Testing PDF Processing Dependencies...")
    print("=" * 50)
    
    # Test 1: Import PyPDF2
    try:
        import PyPDF2
        print("✅ PyPDF2 imported successfully")
        print(f"   Version: {PyPDF2.__version__}")
    except ImportError as e:
        print(f"❌ PyPDF2 import failed: {e}")
        return False
    
    # Test 2: Import pdfplumber
    try:
        import pdfplumber
        print("✅ pdfplumber imported successfully")
        print(f"   Version: {pdfplumber.__version__}")
    except ImportError as e:
        print(f"❌ pdfplumber import failed: {e}")
        return False
    
    # Test 3: Import python-docx
    try:
        import docx
        print("✅ python-docx imported successfully")
    except ImportError as e:
        print(f"❌ python-docx import failed: {e}")
        return False
    
    # Test 4: Test the actual PDF processing function
    try:
        from app import extract_text_from_file
        print("✅ PDF processing function imported successfully")
    except ImportError as e:
        print(f"❌ PDF processing function import failed: {e}")
        return False
    
    print("\n🎉 All PDF processing dependencies are working!")
    print("Your app should work correctly on Render now.")
    return True

def check_requirements_file():
    print("\n📋 Checking requirements.txt...")
    print("=" * 30)
    
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read()
            
        essential_pdf_packages = ['PyPDF2', 'pdfplumber', 'python-docx']
        missing_packages = []
        
        for package in essential_pdf_packages:
            if package in requirements:
                print(f"✅ {package} found in requirements.txt")
            else:
                print(f"❌ {package} missing from requirements.txt")
                missing_packages.append(package)
        
        if not missing_packages:
            print("\n✅ All PDF packages are in requirements.txt!")
            return True
        else:
            print(f"\n❌ Missing packages: {missing_packages}")
            return False
            
    except FileNotFoundError:
        print("❌ requirements.txt not found!")
        return False

if __name__ == "__main__":
    print("🧪 RENDER DEPLOYMENT - PDF PROCESSING TEST")
    print("=" * 45)
    
    # Check requirements.txt
    req_ok = check_requirements_file()
    
    # Test dependencies
    deps_ok = test_pdf_dependencies()
    
    print("\n" + "=" * 45)
    if req_ok and deps_ok:
        print("🎯 RESULT: ✅ READY FOR RENDER DEPLOYMENT!")
        print("\nYour PDF processing will work on Render.")
        print("Push your updated requirements.txt and redeploy.")
    else:
        print("🎯 RESULT: ❌ ISSUES FOUND")
        print("\nFix the issues above before deploying to Render.")
    
    print("\n💡 DEPLOYMENT STEPS:")
    print("1. Run: git add requirements.txt")
    print("2. Run: git commit -m 'Fix PDF processing dependencies'")
    print("3. Run: git push origin main")
    print("4. Redeploy on Render dashboard")
    print("5. Test PDF upload on your live app")
