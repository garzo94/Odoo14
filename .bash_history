git clone https://www.github.com/odoo/odoo --depth 1 --branch 14.0 /opt/odoo14/odoo
python3 -m venv odoo-venv
source odoo-venv/bin/activate
pip3 install -r odoo/requirements.txt
pip3 install wheel
pip3 install -r odoo/requirements.txt
deactivate
mkdir /opt/odoo14/odoo-custom-addons
exit
