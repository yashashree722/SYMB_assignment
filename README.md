# SYMB_assignment

git clone https://github.com/yashashree722/SYMB_assignment.git
cd SYMB_assignment

python -m venv myenv
source myenv/Scripts/activate   # Windows
# OR
source myenv/bin/activate       # Linux/Mac



<!-- install  requirements  -->
pip install -r requirements.txt



<!-- Running the application -->
uvicorn main:app --reload
