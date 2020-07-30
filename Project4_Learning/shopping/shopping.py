import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):

    with open(filename) as f:
        reader =csv.reader(f)
        next(reader)

        data = {'evidence' : [], 'labels': []}

        Month = {'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'June':5, 'Jul':6, 'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11}
        VisitorType = {"Returning_Visitor":1, "New_Visitor":0}
        Weekend = {'TRUE': 1, "FALSE": 0}
        Labels = {"TRUE": 1, "FALSE":0}
        for row in reader:
            evi_list = row[::]
            for i in [0,2,4,11,12,13,14]:
                evi_list[i] = int(evi_list[i])
            for i in [1,3,5,6,7,8,9]:
                evi_list[i]=float(evi_list[i])
            evi_list[10] = Month[evi_list[10]]
            evi_list[16] = Weekend[evi_list[16]]
            if evi_list[15] not in VisitorType.keys():
                evi_list[15]= 0
            else:
                evi_list[15]=VisitorType[evi_list[15]]


            evi_list[17] = Labels[evi_list[17]]

            data['evidence'].append(evi_list[:17])
            data['labels'].append(evi_list[17])

        return(data['evidence'], data['labels'])





def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    true_positive_rate= {
        'lables': 0,
        'predictions': 0
    }
    true_negative_rate = {
        'lables': 0,
        'predictions': 0
    }

    for i in range(len(labels)):
        if labels[i] ==1:
            true_positive_rate['lables'] +=1
            true_positive_rate['predictions'] += predictions[i]
        else:
            true_negative_rate['lables'] += 1
            true_negative_rate['predictions']+= 1- predictions[i]

    sensitivity = true_positive_rate['predictions']/true_positive_rate['lables']
    specificity = true_negative_rate['predictions']/true_negative_rate['lables']

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
