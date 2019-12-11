all:
	pyinstaller -F --distpath . appKiller.py
	sudo rm -r build/ __pycache__/
	sudo rm appKiller.spec

clean:
	rm appKiller

json:
	@echo '{\n\t"app_name" : "test_app.py"\n}' > settings.json
	@echo "settings.json file genarated successfully"