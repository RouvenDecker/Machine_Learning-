
from IPython.display import display, HTML


class HTMLStyler:
    def __init__(self):
        self.css = '''
            <style>
                .applied {
                    color: green;
                }
                .not-applied{
                    color: rgba(102, 75, 98, 0.5);;
                }

                div.styled-div{
                    width: 1000px;
                    border: 10px solid #404141;
                    background-color: white;
                    margin: 5px;
                    padding:5px;
                }

                p,li,dd,dt{
                    color: black;
                    font-size:25px;
                    font-weigth: 500;
                    margin: 5px;
                    width: 700px;
                }

                li{
                    font-size: 27px;
                    width:700px;
                    font-weight:500;
                }
                a{
                    text-decoration: none;
                    color:red;
                    margin: 5px;
                }

                a:hover{
                    color: green;
                }
                a:visited{
                    color: lighted;
                }

                h1 {
                    color: black;
                    margin: 5px;
                    font-weight: 700;
                    font-size:40px;

                }
                h2,dt{
                    color: black;
                    margin: 5px;
                    font-weight: 700;
                    font-size:35px;
                }
                h3{
                    color: black;
                    margin: 5px;
                    font-weight: 700;
                    font-size:30px;
                }
                h4{
                    color: black;
                    margin: 5px;
                    font-weight: 700;
                    font-size:25px;
                }
                article {
                    width: 700px;
                    position:relative;
                    left: 30px;
                    margin: 10px;
                    padding:5px;

                }

                .styled-div.intro{
                    border: 1px solid black;
                    background-color: white;
                    margin: 5px;
                }

                intro {
                    font-size:23px;
                    font-weight:700;
                }
                span#logo{
                    display: inline-block;
                    position: relative;
                    bottom: 20px;
                    right: 20px;
                    padding: 10px;
                    float: left;
                    margin:20px;
                    background-color: white;
                }
                p.highlight{
                    background-color:red;
                    border: 1px solid black;
                    padding:5px;
                    width:300px;
                }
                p.highlight:fist-child()
                {
                    margin:auto;
                }
                tiny{
                    font-size:20px;
                }

            </style>
        '''
        self.box0 = """
        <div class="styled-div">
    	    <img src="./images/ml_pic.svg">
        <div>
        """
        self.box1 = """
        <div class="styled-div">
        <h2>Datastructure in Supervised Learning</h2>
            <article>
                <p>
                    numerical target: <strong>regression</strong><br>
                    categorical target: <strong>classification</strong><br>
                </p>
                <img src="./images/table-img.png" alt="example_table">
                <p class="tiny"><em>source: own</em></p>
            </article>
        </div>
        """
        self.box2 = """
        <div class="styled-div">
            <article>
                <img src="./images/modell-fit.webp" alt="model-fitting">
                <p> source:
                    <a class="tiny" href="https://www.fastaireference.com/overfitting">
                        www.fastaireference.com
                    </a>
                </p>
            </article>
        </div>
        """
        self.box3 = """
        <div class="styled-div">
            <h1> Machine Learning Workflow </h1>
            <article>
                <ol>
                    <li>data exploration</li>
                    <li>data preperation</li>
                    <li>model building</li>
                </ol>
            </article>
        <div>
        """


        self.box4 = '''
        <div class= "styled-div">
            <h2>1. Data Exploration </h2>
            <article>
                <ol>
                    <li class="applied">import dataset</li>
                    <li class="applied">data visualisation</li>
                    <li class="not-applied">statistics</li>
                    <li class="not-applied">outlier identification</li>
                    <li class="not-applied">feature engineering</li>
                </ol>
            </article>
        </div>
        '''
        self.box5 = """
        <div class="styled-div">
            <h3>1.1 Data Load</h3>
        </div>
        """
        self.box6 = """
        <div class="styled-div">
            <h3>block groups</h3>
                <article>
                    <p>
                        Block Groups (BGs) are statistical divisions of census tracts,
                        which are defined to contain <strong> between 600 and 3,000 people</strong><br>
                        <a href='https://www.census.gov/programs-surveys/
                            geography/about/glossary.html#par_textimage_4'
                            title="Data Source">
                            [United States Census Bureau]
                        </a>
                    </p>

                </article>
        </div>
        """
        self.box7 = """
        <div class="styled-div">
        <h3>Dataset Characteristics</h3>
            <article>
                    <p>Datapoints: 20640</p>
                    <p>Features: 8 numeric </p>
                    <p>Targets: 1 numeric (MedHouseVal)</p>
                    <p>Missing Values: 0</p>
                    <a href='https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html' title='Datasource'>
                         [www.dcc.fc.up.pt]
                    </a>
            </article>
        <div>
        """
        self.box8 = """
        <div class="styled-div">
            <h3>Target Description</h3>
            <article>
                <p><strong>MedHouseVal:</strong>
                    in <strong>($100.000)</strong>.<br>
                    This is also the case with <strong>MedInc</strong>.<br>
                     <a href='https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html' title='Datasource'>
                        [www.dcc.fc.up.pt]
                    </a>
                </p>
            </article>
        </div>
        """
        self.box9 = """
        <div class="styled-div">
                <h3>1.2 Visualisation</h3>
        </div>
        """
        self.box10 = """
        <div class="styled-div">
            <h3>Correlation</h3>
                <article>
                    <ul>
                        <li><strong>measure:</strong> relations between 2 Variables</li>
                        <li><strong>good correlation:</strong> between target and feature</li>
                        <li><strong>bad correlation:</strong> between features</li>
                    </ul>
                </article>
        </div>
        """
        self.box11 = """
        <div class="styled-div">
            <h4>checking for bad correlation</h4>
        </div>
        """
        self.box12 = """
        <div class="styled-div">
            <h4>checking for good correlation</h4>
        </div>
        """
        self.box13 = """
        <div class="styled-div">
            <h2>2. Data Preperation</h2>
            <article>
                <ol>
                    <li class ="applied">data cleansing</li>
                    <li class ="not-applied">feature scaling</li>
                    <li class ="applied">train-test-split</li>
                </ol>
            </article>
        </div>
        """
        self.box14 = """
        <div class="styled-div">
            <h3>data cleansing</h3>
            <article>
                <p>
                    remove dataquirks
                </p>
            </article>
        </div>
        """
        self.box15 = """
        <div class="styled-div">
                <h3>2.2 Feature Scaling</h3>
                <h4>standardize</h4>
                <article>
                    <img src="./images/transform.png"
                    alt="z-transformation" height=90 width=200>
                </article>
        </div>"""

        self.box16 = """
        <div class="styled-div">
            <h3>2.3 Train-Test-split </h3>
        </div>
        """
        self.box17 = """
        <div class="styled-div">
            <h2>Modeling</h2>
            <article>
            <ol>
                <li class ="not-applied">build a baseline</li>
                <li class ="applied">scoring</li>
                <li class ="applied">choose a model</li>
                <li class ="not-applied">search hyperparameters</li>
                <li class ="not-applied">crossvalidation</li>

                <li class ="not-applied">change model, retrain,
                compare performances</li>
            </article>
            </ol>
        </div>
        """
        self.box18 = """
        <div class="styled-div">
            <h3>1. Baseline</h3>
        </div>
        """
        self.box19 = """
        <div class="styled-div">
          <h2>2. Scoring (metrics)</h2>
            <article>
                <h4>
                    R2_score ("Bestimmtheitsmaß")
                </h4>
                <p class="highlight">
                    good model : > 0.7
                </p>
                <img class="forms" src="./images/r2.png" alt="r2" width=300 height= 80>
                <h4>
                    Mean Absolute Percentage Error
                </h4>
                <p class ="highlight">
                    good model: < 20 %
                </p>
                <img class="forms" src="./images/mape.png" alt="mape" width=390 height=70>
            </article>
        </div>
        """
        self.box20 = """
        <div class="styled-div">
        <h4>linear Regression score (1 Feature)</h4>
        <div>
        """
        self.box21 = """
        <div class="styled-div">
        <h4>linear Regression score (8 Features)</h4>
        <div>
        """
        self.box22 = """
        <div class="styled-div">
        <h4>Decission Tree Regressor (8 Features)</h4>
        <div>
        """
        self.box23 = """
        <div class="styled-div">
            <h3>GraphvizTreePlot</h3>
        <div>
        """
        self.box24 = """
        <div class="styled-div">
        <h3>Exporting the model</h3>
        <div>
        """
        self.box25 = """
        <div class="styled-div">
        <h4>save</h4>
        <div>
        """
        self.box26 = """
        <div class="styled-div">
        <h4>load</h4>
        <div>
        """
        self.box27 ="""
        <div class="styled-div">
            <h3>Book Sources</h3>
            <article>
                <h4>practice</h4>
                <p>
                    Aurélien Gèron - Hands-on Machine Learning
                    with Scikit-Learn,
                    Keras & Tensorflow
                </p>
                <h4>theory</h4>
                <p>
                    Trevor Hastie, Robert Tibshirani, Jerome Friedman
                    - The Elements of Statistical Learning (Data Mining,
                    Inference, and Prediction)
                </p>
            </article
        <div>
        """
        self.box28 = """
        <div class="styled-div">
            <h3>Ensemble learning without Further Tweaks</h3>
        <div>
        """
        self.box28 = """
        <div class="styled-div">
            <h3>Ensemble learning with Further Tweaks</h3>
        <div>
        """

    def exec_styled_cell(self, number) -> None:
        match number:
            case 0:
                display(HTML(self.css + self.box0))
            case 1:
                display(HTML(self.css + self.box1))
            case 2:
                display(HTML(self.css + self.box2))
            case 3:
                display(HTML(self.css + self.box3))
            case 4:
                display(HTML(self.css + self.box4))
            case 5:
                display(HTML(self.css + self.box5))
            case 6:
                display(HTML(self.css + self.box6))
            case 7:
                display(HTML(self.css + self.box7))
            case 8:
                display(HTML(self.css + self.box8))
            case 9:
                display(HTML(self.css + self.box9))
            case 10:
                display(HTML(self.css + self.box10))
            case 11:
                display(HTML(self.css + self.box11))
            case 12:
                display(HTML(self.css + self.box12))
            case 13:
                display(HTML(self.css + self.box13))
            case 14:
                display(HTML(self.css + self.box14))
            case 15:
                display(HTML(self.css + self.box15))
            case 16:
                display(HTML(self.css + self.box16))
            case 17:
                display(HTML(self.css + self.box17))
            case 18:
                display(HTML(self.css + self.box18))
            case 19:
                display(HTML(self.css + self.box19))
            case 20:
                display(HTML(self.css + self.box20))
            case 21:
                display(HTML(self.css + self.box21))
            case 22:
                display(HTML(self.css + self.box22))
            case 23:
                display(HTML(self.css + self.box23))
            case 24:
                display(HTML(self.css + self.box24))
            case 25:
                display(HTML(self.css + self.box25))
            case 26:
                display(HTML(self.css + self.box26))
            case 27:
                display(HTML(self.css + self.box27))
            case 28:
                display(HTML(self.css + self.box28))
            case _:
                print("invalid")
