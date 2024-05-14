# FastAPI Logging

```sh
$ poetry run python src/main.py

2024-05-14 15:33:43,038	DEBUG			selector_events.py::__init__::54
		Using selector: KqueueSelector
2024-05-14 15:33:43,052	INFO			server.py::_serve::82
		Started server process [12991]
2024-05-14 15:33:43,052	INFO			on.py::startup::48
		Waiting for application startup.
2024-05-14 15:33:43,052	INFO			on.py::startup::62
		Application startup complete.
2024-05-14 15:33:43,053	INFO			server.py::_log_started_message::214
		Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```


```sh
 $ curl http://localhost:8000/wait/6/ -X POST
{"message":"Task[6]"}%
```


```sh
2024-05-14 15:36:24,336	DEBUG			main.py::wait::32
		Debug from Task[6]
2024-05-14 15:36:24,336	INFO			main.py::wait::33
		Info from Task[6]
2024-05-14 15:36:24,336	WARNING			main.py::wait::34
		Warning from Task[6]
2024-05-14 15:36:24,336	ERROR			main.py::wait::35
		Error from Task[6]
2024-05-14 15:36:24,336	CRITICAL			main.py::wait::36
		Critical from Task[6]
2024-05-14 15:36:24,337	INFO			main.py::wait::40
		Task[6] added
2024-05-14 15:36:24,337	INFO			h11_impl.py::send::477
		127.0.0.1:50566 - "POST /wait/6/ HTTP/1.1" 200
2024-05-14 15:36:24,337	INFO			main.py::sleep_and_log::24
		Wait 6 seconds...
2024-05-14 15:36:30,337	INFO			main.py::sleep_and_log::26
		done!
```


---

Modern Python loggin tips (from [mCoding](https://www.youtube.com/watch?v=9L77QExPmI0)):
- Use [dictConfig](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig);
- Put all Handlers/Filters on the root logger;
- Don't use the root logger;
- One logger per majob subcomponent;