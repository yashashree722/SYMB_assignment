

Clone Repo     
git clone https://github.com/yashashree722/SYMB_assignment.git    
cd SYMB_assignment     

2. Create a Virtual Environment        
python -m venv myenv    
source myenv/Scripts/activate    


Linux/Mac        
python -m venv myenv
source myenv/bin/activate


Install Dependencies
pip install -r requirements.txt


Running the Application
uvicorn main:app --reload


The API will be accessible at: http://127.0.0.1:8000
