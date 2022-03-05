## Instructions
1) Create a Docker container that runs a HTTP API on TCP port 8080.
1) Design the API so it exposes the following endpoints:
	- listing all readings
	- retrieving an existing reading
	- adding a new reading
	- modifying existing reading
	- deleting existing reading
	- retrieve statistics of readings in a specific time window (see below for statistics)
	
		Reading object:
			id: int,
			value: float,
			timestamp: datetime
		
  	- At least the following statistics need to be calculated (can do more):
		- reading count
		- mean
		- variance
	- select one of statistical tests that test data for Gaussian distribution, and check if given data is drawn from Normal distribution (choose reasonable p-value threshold yourself)
	- if data comes from Normal distribution, calculate confidence interval (choose confidence threshold yourself)
	- select one of statistical tests that test data for stationarity, and check if given time series is stationary (choose p-value threshold yourself)
	
1) Optional: include a pytest test (no need for extensive coverage - just a sample)
## Notes
- Use Python, Flask for the API service.
- Persistent store is not required, use runtime data structures (if you decide to use persistent store such as SQLite and ORM such SQLAlchemy - this would be a bonus).
- If you feel some detail is missing, feel free to make your own decisions (documenting them in README).
## Deliverable
An archive containing:
		- concise README.TXT containing
			- instructions how to start the service
			- a list of supported endpoints with request parameters and expected responses
			- anything else you deem necessary
		- Dockerfile
		- Python file(-s)
		- Anything else required to launch the service (scripts, configuration files)
## Assessment
- Clear instructions in README.TXT
- API design adherence to REST API best practices
- Request, calculation errors are handled gracefully
- Code readability
- Right choice of statistical methods
- Any additional improvement, initiative is very welcome!