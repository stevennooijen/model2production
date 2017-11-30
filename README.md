# EventBrite fraud

The goal of this exercise is to get hands-on experience with building a predictive model and wrapping it into an API.
At the end of today, you'll not only have created and validated your model, but also implemented it as part of an API 
that returns predictions for unseen data.

## Workflow

* Create your own central git repository (on Github) and make two clones of it, 
    one locally and one on the server;
* Build model and API in the local repo;
* Make sure you model & API work in the local repo;
* Commit to the local git repository;
* Push to your central repo;
* Pull changes on your server repo and (re-)deploy;
* Improve your model (GridSearchCV) & API locally;
* Redeploy best model 

## Lessons learned

- Start with simple Flask app that returns static predictions to test API. 
    See `api/example/example_with_resource.py`
- Test Flask locally with `debug=True` and `print()` statements.
- Call your Flask app from notebooks with the `requests` library. Easy to add arguments.
- Flask app runs by default on localhost. Add `host='0.0.0.0'` in `app.run()` to run on your 
    machine's IP address.  
- Expand static Flask app gradually. First try with a very simple model.
- With more advanced models: don't forget to change the request parsing in the `app.py`.
- Create a nice and tidy project structure