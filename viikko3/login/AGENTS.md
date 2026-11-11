Repository-specific notes for OpenCode agents

Top-level project: viikko3/login — a small Flask app with Robot Framework browser (Playwright) tests. Run commands with uv run. Do not install dependencies independently.

Important runtime facts an agent would otherwise miss
- App entrypoint: src/index.py — run it from viikko3/login (so imports resolve):
  - python src/index.py
  - The server binds to port 5001 by default (app.run(port=5001, host="0.0.0.0")). Do not change the port unless you also update the Robot tests.
- Test reset endpoint: POST http://localhost:5001/tests/reset clears repository state for tests. Useful to call between runs (tests already call it).

Robot Framework browser tests (important gotchas)
- Tests live in src/tests and use the Robot Browser library (Playwright). The tests assume the web server is running at localhost:5001 (see src/tests/resource.robot ${SERVER}).
- Typical test flow (two terminals):
  1) Start the app: python src/index.py
  2) In another terminal run tests: robot src/tests
- Headless / CI: resource.robot sets ${HEADLESS} to false by default. On CI use:
  - robot -v HEADLESS:true src/tests
- Running a single Robot test or case:
  - robot -t "Test Case Name" src/tests/login.robot
  - or: robot -t "Login With Correct Credentials" src/tests/login.robot

The validation of username and password happens at method validate in src/services/user_service.py