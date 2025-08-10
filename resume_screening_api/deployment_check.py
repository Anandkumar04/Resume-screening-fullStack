"""
Pre-Deployment Checklist for Resume Screening AI
"""
import os
import sys

def deployment_readiness_check():
    print("🚀 DEPLOYMENT READINESS CHECK")
    print("="*50)
    
    checklist = {
        "✅ Passed": [],
        "⚠️  Warning": [],
        "❌ Failed": []
    }
    
    # 1. Check core application files
    print("📁 Checking Core Files...")
    core_files = [
        'app.py',
        'templates/index.html',
        'templates/about.html',
        'requirements.txt'
    ]
    
    for file in core_files:
        if os.path.exists(file):
            checklist["✅ Passed"].append(f"Core file: {file}")
        else:
            checklist["❌ Failed"].append(f"Missing core file: {file}")
    
    # 2. Check model files
    print("🤖 Checking ML Model Files...")
    model_files = [
        'models/resume_classifier.pkl',
        'models/tfidf_vectorizer.pkl',
        'models/label_encoder.pkl'
    ]
    
    for file in model_files:
        if os.path.exists(file):
            size_mb = os.path.getsize(file) / (1024*1024)
            checklist["✅ Passed"].append(f"Model file: {file} ({size_mb:.1f} MB)")
        else:
            checklist["❌ Failed"].append(f"Missing model file: {file}")
    
    # 3. Check supporting files
    print("📄 Checking Supporting Files...")
    support_files = [
        'models/train_model.py',
        'preprocessing/text_cleaner.py',
        'utils/model_utils.py'
    ]
    
    for file in support_files:
        if os.path.exists(file):
            checklist["✅ Passed"].append(f"Support file: {file}")
        else:
            checklist["⚠️  Warning"].append(f"Optional file missing: {file}")
    
    # 4. Check dataset
    print("📊 Checking Dataset...")
    if os.path.exists('../resume_dataset.csv'):
        size_mb = os.path.getsize('../resume_dataset.csv') / (1024*1024)
        checklist["✅ Passed"].append(f"Dataset: resume_dataset.csv ({size_mb:.1f} MB)")
    else:
        checklist["⚠️  Warning"].append("Dataset file not in expected location")
    
    # 5. Check requirements.txt
    print("📦 Checking Dependencies...")
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            requirements = f.read()
            essential_packages = ['flask', 'scikit-learn', 'pandas', 'nltk', 'numpy']
            missing_packages = []
            
            for package in essential_packages:
                if package.lower() not in requirements.lower():
                    missing_packages.append(package)
            
            if not missing_packages:
                checklist["✅ Passed"].append("All essential packages in requirements.txt")
            else:
                checklist["⚠️  Warning"].append(f"Potentially missing packages: {missing_packages}")
    
    # 6. Security check
    print("🔒 Security Check...")
    if os.path.exists('app.py'):
        with open('app.py', 'r') as f:
            app_content = f.read()
            
            if 'debug=True' in app_content and 'host=' in app_content:
                checklist["⚠️  Warning"].append("Debug mode enabled - disable for production")
            else:
                checklist["✅ Passed"].append("Production-safe Flask configuration")
            
            if 'MAX_CONTENT_LENGTH' in app_content:
                checklist["✅ Passed"].append("File upload size limits configured")
            else:
                checklist["⚠️  Warning"].append("Consider adding file upload limits")
    
    # 7. Performance check
    print("⚡ Performance Check...")
    total_model_size = 0
    for file in model_files:
        if os.path.exists(file):
            total_model_size += os.path.getsize(file)
    
    total_size_mb = total_model_size / (1024*1024)
    if total_size_mb < 50:
        checklist["✅ Passed"].append(f"Model size acceptable: {total_size_mb:.1f} MB")
    elif total_size_mb < 100:
        checklist["⚠️  Warning"].append(f"Large model size: {total_size_mb:.1f} MB - consider optimization")
    else:
        checklist["❌ Failed"].append(f"Model too large: {total_size_mb:.1f} MB")
    
    # Print results
    print("\n" + "="*50)
    print("📋 DEPLOYMENT READINESS RESULTS")
    print("="*50)
    
    for status, items in checklist.items():
        if items:
            print(f"\n{status}:")
            for item in items:
                print(f"   • {item}")
    
    # Overall assessment
    failed_count = len(checklist["❌ Failed"])
    warning_count = len(checklist["⚠️  Warning"])
    passed_count = len(checklist["✅ Passed"])
    
    print(f"\n📊 SUMMARY:")
    print(f"   ✅ Passed: {passed_count}")
    print(f"   ⚠️  Warnings: {warning_count}")
    print(f"   ❌ Failed: {failed_count}")
    
    if failed_count == 0:
        if warning_count <= 2:
            deployment_status = "🚀 READY FOR DEPLOYMENT"
            recommendation = "Your application is production-ready!"
        else:
            deployment_status = "⚠️  MOSTLY READY"
            recommendation = "Address warnings for optimal deployment"
    else:
        deployment_status = "❌ NOT READY"
        recommendation = "Fix critical issues before deployment"
    
    print(f"\n{deployment_status}")
    print(f"Recommendation: {recommendation}")
    
    return {
        'status': deployment_status,
        'passed': passed_count,
        'warnings': warning_count,
        'failed': failed_count
    }

if __name__ == "__main__":
    try:
        results = deployment_readiness_check()
        print(f"\n✅ Deployment check completed!")
    except Exception as e:
        print(f"\n❌ Error during deployment check: {e}")
        import traceback
        traceback.print_exc()
