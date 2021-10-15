##############
#Summary Stats
##############
def summarize(dataframe,variable):
    #dependencies
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    #define arguments
    dfvar=dataframe[variable]
    description=dfvar.describe()
    print(description)
    print("\n")
    checkset=dataframe.dropna(subset=[variable])
    checkvar=dfvar.dropna().copy(deep=True)
    if (checkvar % 1  == 0).all()== True and len(set(checkvar))<10:
        cats=set(checkvar)
        print("Obs per category")
        print("------------------")
        for item in cats:
           count=len(dataframe.loc[dfvar == item])
           percent=round(count/len(dfvar)*100, 2)
           print(f"{item}-> {count} ({percent}%)")

        x = set(checkvar)
        heightlist=[]
        for value in x:
            heightlist.append(len(checkset.loc[checkset[variable] == value]))

        x_pos = [i for i, _ in enumerate(x)]
        plt.barh(x_pos, heightlist, color='green')
        plt.yticks(x_pos, x)
        plt.show()

    else:
        hist=plt.hist(dfvar, bins=10)
        plt.show()
        print(hist)
#######################################################################
#Numerify
#Turns all categorical variables to numeric with reference category "0"
########################################################################
def numerify(dataframe):
    for thing in dataframe.columns:
        var=dataframe[thing]
        has_string=False
        values=set(dataframe[thing])
        for item in var:
            if type(item)==str:
                has_string=True
                break
        if has_string == True:
            counter=0
            for item in values:
                dataframe.replace(to_replace=item, value=counter, inplace=True)
                counter+=1
        elif (var.fillna(-9999) % 1  == 0).all()== False:
            counter=0
            for item in values:
                dataframe.replace(to_replace=item, value=counter, inplace=True)
                counter+=1
        else:
            continue
 #################           
#Linear Regression
##################
#Arg 1 = dataset, Args 2-N = "variable" (name in quotes)

def regress(*args):
    #import dependencies
    import sklearn as sk
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    from sklearn import feature_selection
    import statsmodels.api as sm
    from patsy import dmatrices
    import matplotlib.pyplot as plt

    #define arguments
    dataframe=args[0]
    y=args[1]
    xvars=[]
    for i in range(2,len(args)):
        xvars.append(args[i])
    x = dataframe[[item for item in xvars]]
    y = dataframe[y].values.reshape(-1, 1)
    #fit the model
    model.fit(x,y)

    #Generate Fit Statistics
    ##prep data for patsy
    list=[]
    for item in xvars:
        list.append(f' + {item}')
    string="".join(list)
    newstring=string[3:]

    ind=args[1]
    ind=ind.strip('"')

    ##Get fitstats from patsy
    Y,X = dmatrices(f"{ind} ~ {newstring}", data=dataframe, return_type="dataframe")
    ols = sm.OLS(Y, X)
    ols_result = ols.fit()
    print(ols_result.summary())

    #Plot the Residuals
    print("\n Residual Plot")
    predictions = model.predict(x)
    plt.scatter(predictions, predictions - y, color='coral',linewidths=0.5)
    plt.hlines(y=0, xmin=predictions.min(), xmax=predictions.max(), color='brown', linewidth=3)
    plt.show()

#####################
#Logistic Regression
#####################
#Arg 1 = dataset, Args 2-N = "variable" (name in quotes)

def linregress(*args):
    #import dependencies
    import sklearn as sk
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    from sklearn import feature_selection
    import statsmodels.api as sm
    from patsy import dmatrices
    import numpy as np

    #define arguments
    dataframe=args[0]
    y=args[1]
    xvars=[]
    for i in range(2,len(args)):
        xvars.append(args[i])
    x = dataframe[[item for item in xvars]]
    y = dataframe[y]
    #fit the model
    model.fit(x,y)
    
    #Generate Fit Statistics
    ##prep data for patsy
    list=[]
    for item in xvars:
        list.append(f' + {item}')
    string="".join(list)
    newstring=string[3:]

    ind=args[1]
    ind=ind.strip('"')

    ##Fit the Model
    Y,X = dmatrices(f"{ind} ~ {newstring}", data=dataframe, return_type="dataframe")
    logit = sm.Logit(Y, X)
    logit_result = logit.fit()

    #Print Log Odds
    print("LOG ODDS")
    print(logit_result.summary())
    print(np.exp(logit_result.params))

    #Plot the Residuals
    print("\n Residual Plot")
    from sklearn.linear_model import Ridge
    from yellowbrick.datasets import load_concrete
    from yellowbrick.regressor import ResidualsPlot
    
    model = Ridge()

    visualizer = ResidualsPlot(model, hist=True)
    y2= y.values.reshape(-1, 1)
    visualizer.fit(x, y2)  # Fit the training data to the visualizer
    visualizer.score(x, y2)  # Evaluate the model on the test data
    visualizer.show()                 # Finalize and render the figure

    #predictions = model.predict(x)
    #plt.scatter(predictions, predictions - y, color='coral',linewidths=0.5)
    #plt.hlines(y=0, xmin=predictions.min(), xmax=predictions.max(), color='brown', linewidth=3)
    #plt.show()


