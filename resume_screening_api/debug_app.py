from flask import Flask, request, jsonify
import traceback

app = Flask(__name__)

@app.route('/debug-predict', methods=['POST'])
def debug_predict():
    """Debug version of predict endpoint"""
    try:
        print("=== DEBUG PREDICT ENDPOINT ===")
        print(f"Request method: {request.method}")
        print(f"Content type: {request.content_type}")
        print(f"Form data: {dict(request.form)}")
        print(f"Files: {list(request.files.keys())}")
        
        # Test basic form data access
        if 'resume_text' in request.form:
            text = request.form['resume_text']
            print(f"Found resume_text with length: {len(text)}")
            return jsonify({
                'status': 'success',
                'message': 'Text received',
                'text_length': len(text),
                'text_preview': text[:100]
            })
        else:
            print("No resume_text found in form")
            return jsonify({
                'status': 'error',
                'message': 'No resume_text in form data',
                'available_keys': list(request.form.keys())
            }), 400
            
    except Exception as e:
        print(f"Exception in debug endpoint: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <h1>Debug Resume Screening</h1>
        <form method="POST" action="/debug-predict">
            <textarea name="resume_text" rows="10" cols="50" placeholder="Enter resume text">Python developer with machine learning experience</textarea><br><br>
            <button type="submit">Test Predict</button>
        </form>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
