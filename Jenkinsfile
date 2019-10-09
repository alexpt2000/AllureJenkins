timestamps {
    node(){
	stage ('Checkout'){
	    checkout scm	
	}	
	
        stage ('Setup virtualenv') {
            sh """
            PATH=$WORKSPACE/venv/bin:/anaconda3/bin:$PATH
            if [ ! -d "venv" ]; then
                    python3 -m virtualenv venv
            fi
            . venv/bin/activate
	    which python 

            python -m pip install -r requirements.txt -r test/test_requirements.txt
            """
        }

        stage ('Run Tests'){
            sh """
            . venv/bin/activate
            which python

            nosetests --with-allure --with-coverage --logdir=./allure-results ./test
            """

        }

        stage ('Run MyPy'){
            sh """
            . venv/bin/activate
            which python

            mypy src --junit-xml ./allure-results/mypy.xml
            """
        }

        stage ('Run Flakes8') {
            sh """
            . venv/bin/activate
            which python

            cd src
            flake8 --output-file ../allure-results/flake8.txt || true
            cd ..

            cd allure-results
            flake8_junit flake8.txt flake8_junit.xml
            """
        }

        stage ('Publish Allure Report'){
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}