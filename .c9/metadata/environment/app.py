{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":12,"column":0},"end":{"row":13,"column":48},"action":"remove","lines":["app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv(\"MONGO_URI\")"],"id":1245},{"start":{"row":12,"column":0},"end":{"row":13,"column":71},"action":"insert","lines":["app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')"]}],[{"start":{"row":27,"column":0},"end":{"row":29,"column":0},"action":"remove","lines":["    _tasks = mongo.db.tasks.find()","    task_list = [task for task in _tasks]",""],"id":1246}],[{"start":{"row":27,"column":47},"end":{"row":27,"column":56},"action":"remove","lines":["task_list"],"id":1247},{"start":{"row":27,"column":47},"end":{"row":27,"column":74},"action":"insert","lines":["tasks=mongo.db.tasks.find()"]}],[{"start":{"row":27,"column":46},"end":{"row":27,"column":47},"action":"remove","lines":["="],"id":1248},{"start":{"row":27,"column":45},"end":{"row":27,"column":46},"action":"remove","lines":["s"]},{"start":{"row":27,"column":44},"end":{"row":27,"column":45},"action":"remove","lines":["k"]},{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"remove","lines":["s"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"remove","lines":["a"]},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"remove","lines":["t"]}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["    # Create variables and pass that in to the render_template() method",""],"id":1249}],[{"start":{"row":33,"column":0},"end":{"row":36,"column":0},"action":"remove","lines":["    # Create variables and pass that in to the method","    _categories = mongo.db.categories.find()","    category_list = [category for category in _categories]",""],"id":1250}],[{"start":{"row":33,"column":43},"end":{"row":33,"column":67},"action":"remove","lines":["categories=category_list"],"id":1251},{"start":{"row":33,"column":43},"end":{"row":33,"column":80},"action":"insert","lines":["categories=mongo.db.categories.find()"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1560116876651,"hash":"c10dfcaa98e86223f621e41776787138493bdfc9"}