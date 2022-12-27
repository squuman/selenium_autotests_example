# install python packages
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# download allure
wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip
unzip allure-2.13.8.zip
rm allure-2.13.8.zip
mkdir report
mkdir drivers