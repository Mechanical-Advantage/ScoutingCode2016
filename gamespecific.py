import numpy as np
import sqlite3 as sql

#Defines the fields stored in the "Scout" table of the database. This database stores the record for each match scan
SCOUT_FIELDS = {
    "Team": 0,
    "Match": 0,
    "Fouls": 0,
    "TechFouls": 0,
    "Replay": 0,
    "Flag": 0,
    "AllianceColor": 0,
    "StartPos": 0,
    "CrossedLine": 0,
    "AutoBalltoTowerHighSuccess": 0,
    "AutoBalltoTowerHighFailure": 0,
    "AutoBalltoTowerLowSuccess": 0,
    "AutoBalltoTowerLowFailure": 0,
    "AutoCrossedDefensePC": 0,
    "AutoCrossedDefenseCDF": 0,
    "AutoCrossedDefenseMT": 0,
    "AutoCrossedDefenseRPT": 0,
    "AutoCrossedDefensePDB": 0,
    "AutoCrossedDefenseSP": 0,
    "AutoCrossedDefenseRW": 0,
    "AutoCrossedDefenseLB": 0,
    "AutoCrossedDefenseBar": 0,
    "TeleOPBalltoTowerHighSuccess": 0,
    "TeleOPBalltoTowerHighFailure": 0,
    "TeleOPBalltoTowerLowSuccess": 0,
    "TeleOPBalltoTowerLowFailure": 0,
    "TeleOPCrossedDefensePC": 0,
    "TeleOPCrossedDefenseCDF": 0,
    "TeleOPCrossedDefenseMT": 0,
    "TeleOPCrossedDefenseRPT": 0,
    "TeleOPCrossedDefensePDB": 0,
    "TeleOPCrossedDefenseSP": 0,
    "TeleOPCrossedDefenseRW": 0,
    "TeleOPCrossedDefenseLB": 0,
    "TeleOPCrossedDefenseBar": 0,
    "ClimbAchieved": 0,
	"ClimbAttempt": 0,
    "WonMatch": 0,
    "ParkAttempt": 0,
	"ParkAchieved": 0,
    "Disabled": 0,
    "DriverRating": 0,
    "IntakeRating": 0,
    "DeliverySpeedRating": 0,
    "DefenseRating": 0,
    "AvoidDefenseRating": 0,
    "RatingCrossedDefensePC": 0,
    "RatingCrossedDefenseCDF": 0,
    "RatingCrossedDefenseMT": 0,
    "RatingCrossedDefenseRPT": 0,
    "RatingCrossedDefensePDB": 0,
    "RatingCrossedDefenseSP": 0,
    "RatingCrossedDefenseRW": 0,
    "RatingCrossedDefenseLB": 0,
    "RatingCrossedDefenseBar": 0
}

#Defines the fields that are stored in the "averages" and similar tables of the database. These are the fields displayed on the home page of the website.
AVERAGE_FIELDS = {
    "team": 0,
    "apr":0,
    "AutoCrossedDefensePC": 0,
    "AutoCrossedDefenseCDF": 0,
    "AutoCrossedDefenseMT": 0,
    "AutoCrossedDefenseRPT": 0
}

#Defines the fields displayed on the charts on the team and compare pages
CHART_FIELDS = {
    "match": 0,
    "AutoCrossedDefensePC": 0,
    "AutoCrossedDefenseCDF": 0,
    "AutoCrossedDefenseMT": 0,
    "AutoCrossedDefenseRPT": 0
}


# Main method to process a full-page sheet
# Submits three times, because there are three matches on one sheet
# The sheet is developed in Google Sheets and the coordinates are defined in terms on the row and column numbers from the sheet.
def processSheet(scout):
    for s in (0, 23):
        #Sets the shift value (used when turning cell coordinates into pixel coordinates)
        scout.shiftDown(s)

        num1 = scout.rangefield('J-5', 0, 9)
        num2 = scout.rangefield('J-6', 0, 9)
        num3 = scout.rangefield('J-7', 0, 9)
        num4 = scout.rangefield('J-8', 0, 9)
        scout.set("Team", 1000 * num1 + 100 * num2 + 10 * num3 + num4)

        match1 = scout.rangefield('AB-5', 0, 1)
        match2 = scout.rangefield('AB-6', 0, 9)
        match3 = scout.rangefield('AB-7', 0, 9)
        scout.set("Match", 100 * match1 + 10 * match2 + match3)

        scout.set("Fouls", int(0))
        scout.set("TechFouls", int(0))


        scout.set("AllianceColor", scout.rangefield('L-10', 0, 1))
        scout.set("StartPos", scout.rangefield('F-10', 1, 3)-1)
        scout.set("CrossedLine", scout.boolfield('P-10'))
        scout.set("AutoBalltoTowerHighSuccess", scout.rangefield('T-10',1,3))
        scout.set("AutoBalltoTowerHighFailure", scout.rangefield('T-11',1,3))
        scout.set("AutoBalltoTowerLowSuccess", scout.rangefield('X-10',1,3))
        scout.set("AutoBalltoTowerLowFailure", scout.rangefield('X-11',1,3))
        scout.set("AutoCrossedDefensePC", scout.rangefield('AB-11',1,2))
        scout.set("AutoCrossedDefenseCDF", scout.rangefield('AC-11',1,2))
        scout.set("AutoCrossedDefenseMT", scout.rangefield('AD-11',1,2))
        scout.set("AutoCrossedDefenseRPT", scout.rangefield('AE-11',1,2))
        scout.set("AutoCrossedDefensePDB", scout.rangefield('AF-11',1,2))
        scout.set("AutoCrossedDefenseSP", scout.rangefield('AG-11',1,2))
        scout.set("AutoCrossedDefenseRW", scout.rangefield('AH-11',1,2))
        scout.set("AutoCrossedDefenseLB", scout.rangefield('AI-11',1,2))
        scout.set("AutoCrossedDefenseBar", scout.rangefield('AJ-11',1,2))
        scout.set("TeleOPBalltoTowerHighSuccess", scout.rangefield('F-14',1,8))
        scout.set("TeleOPBalltoTowerHighFailure", scout.rangefield('F-15',1,8))
        scout.set("TeleOPBalltoTowerLowSuccess", scout.rangefield('F-18',1,8))
        scout.set("TeleOPBalltoTowerLowFailure", scout.rangefield('F-19',1,8))
        scout.set("TeleOPCrossedDefensePC", scout.rangefield('Q-16',1,2))
        scout.set("TeleOPCrossedDefenseCDF", scout.rangefield('R-16',1,2))
        scout.set("TeleOPCrossedDefenseMT", scout.rangefield('S-16',1,2))
        scout.set("TeleOPCrossedDefenseRPT", scout.rangefield('T-16',1,2))
        scout.set("TeleOPCrossedDefensePDB", scout.rangefield('U-16',1,2))
        scout.set("TeleOPCrossedDefenseSP", scout.rangefield('V-16',1,2))
        scout.set("TeleOPCrossedDefenseRW", scout.rangefield('W-16',1,2))
        scout.set("TeleOPCrossedDefenseLB", scout.rangefield('X-16',1,2))
        scout.set("TeleOPCrossedDefenseBar", scout.rangefield('Y-16',1,2))

        scout.set("WonMatch", scout.boolfield('F-24'))
        scout.set("ClimbAttempt", scout.boolfield('G-21'))
        scout.set("ClimbAchieved", scout.boolfield('G-22'))
        scout.set("ParkAttempt", scout.boolfield('L-21',))
        scout.set("ParkAchieved", scout.boolfield('L-22',))
        scout.set("Disabled", scout.boolfield('F-25'))

        scout.set("DriverRating", scout.rangefield('AD-15', 0, 5))
        scout.set("IntakeRating", scout.rangefield('AD-16', 0, 5))
        scout.set("DeliverySpeedRating", scout.rangefield('AD-17', 0, 5))
        scout.set("DefenseRating", scout.rangefield('AD-18', 0, 5))
        scout.set("AvoidDefenseRating", scout.rangefield('AD-19', 0, 5))
        scout.set("RatingCrossedDefensePC", scout.rangefield('0-21', 0,5))
        scout.set("RatingCrossedDefenseCDF", scout.rangefield('P-21', 0,5))
        scout.set("RatingCrossedDefenseMT", scout.rangefield('Q-21', 0,5))
        scout.set("RatingCrossedDefenseRPT", scout.rangefield('R-21', 0,5))
        scout.set("RatingCrossedDefensePDB", scout.rangefield('S-21', 0,5))
        scout.set("RatingCrossedDefenseSP", scout.rangefield('T-21', 0,5))
        scout.set("RatingCrossedDefenseRW", scout.rangefield('U-21', 0, 5))
        scout.set("RatingCrossedDefenseLB", scout.rangefield('V-21',0, 5))
        scout.set("RatingCrossedDefenseBar", scout.rangefield('W-21',0, 5))

        scout.set("Replay", scout.boolfield('AK-5'))

        scout.submit()


#Takes an entry from the Scout database table and generates text for display on the team page. This page has 4 columns, currently used for auto, 2 teleop, and other (like fouls and end game)
def generateTeamText(e):
    text = {'auto': "", 'teleop1': "", 'teleop2': "", 'other': ""}
    text['auto'] += 'baseline, ' if e['AutoCrossedDefensePC'] else ''
    text['auto'] += 'Switch try, ' if e['AutoCrossedDefenseCDF'] else ''
    text['auto'] += 'Scale try, ' if e['AutoCrossedDefenseMT'] else ''
    text['auto'] += 'Exchange try, ' if e['AutoCrossedDefenseRPT'] else ''

    text['teleop1'] += str(
        e['AutoCrossedDefensePC']) + 'x to scale, ' if e['AutoCrossedDefensePC'] else ''

    text['teleop2'] += str(
        e['AutoCrossedDefenseCDF']) + 'to switch, ' if e['AutoCrossedDefenseCDF'] else ''
    text['teleop2'] += str(
        e['AutoCrossedDefenseMT']) + 'to opp switch, ' if e['AutoCrossedDefenseMT'] else ''

    text['other'] = 'Climb, ' if e['Climb'] else ' '


    return text


#Takes an entry from the Scout database table and generates chart data. The fields in the returned dict must match the CHART_FIELDS definition at the top of this file
def generateChartData(e):
    dp = dict(CHART_FIELDS)
    dp["match"] = e['match']

    dp['AutoCrossedDefensePC'] += e['AutoCrossedDefensePC']
    dp['AutoCrossedDefenseCDF'] += e['AutoCrossedDefenseCDF']
    dp['AutoCrossedDefenseMT'] += e['AutoCrossedDefenseMT']
    dp['AutoCrossedDefenseRPT'] += e['AutoCrossedDefenseRPT']

    return dp


#Takes a set of team numbers and a string indicating quals or playoffs and returns a prediction for the alliances score and whether or not they will achieve any additional ranking points
def predictScore(datapath, teams, level='quals'):
    conn = sql.connect(datapath)
    conn.row_factory = sql.Row
    cursor = conn.cursor()
    ballScore = []
    endGame = []
    autoGears = []
    teleopGears = []
    for n in teams:
        average = cursor.execute('SELECT * FROM averages WHERE team=?',
                                 (n, )).fetchall()
        assert len(average) < 2
        if len(average):
            entry = average[0]
        else:
            entry = [0] * 8
        autoGears.append(entry[2])
        teleopGears.append(entry[3])
        ballScore.append((entry[5] + entry[6]))
        endGame.append((entry[7]))
    retVal = {'score': 0, 'gearRP': 0, 'fuelRP': 0}
    score = sum(ballScore[0:3]) + sum(endGame[0:3])
    if sum(autoGears[0:3]) >= 1:
        score += 60
    else:
        score += 40
    if sum(autoGears[0:3]) >= 3:
        score += 60
    elif sum(autoGears[0:3] + teleopGears[0:3]) >= 2:
        score += 40
    if sum(autoGears[0:3] + teleopGears[0:3]) >= 6:
        score += 40
    if sum(autoGears[0:3] + teleopGears[0:3]) >= 12:
        score += 40
        if level == 'playoffs':
            score += 100
        else:
            retVal['gearRP'] == 1
    if sum(ballScore[0:3]) >= 40:
        if level == 'playoffs':
            score += 20
        else:
            retVal['fuelRP'] == 1
    retVal['score'] = score
    return retVal


#Takes an entry from the Scout table and returns whether or not the entry should be flagged based on contradictory data.
def autoFlag(entry):
#    if (entry['AutoHighBalls']
#            or entry['TeleopHighBalls']) and (entry['AutoLowBalls']
#                                              or entry['AutoHighBalls']):
#        return 1
#    if entry['Hang'] and entry['FailedHang']:
#        return 1
    return 0


#Takes a list of Scout table entries and returns a nested dictionary of the statistical calculations (average, maxes, median, etc.) of each field in the AVERAGE_FIELDS definition
def calcTotals(entries):
    sums = dict(AVERAGE_FIELDS)
    noDefense = dict(AVERAGE_FIELDS)
    lastThree = dict(AVERAGE_FIELDS)
    noDCount = 0
    lastThreeCount = 0
    for key in sums:
        sums[key] = []
    #For each entry, add components to the running total if appropriate
    for i, e in enumerate(entries):
        sums['AutoCrossedDefensePC'].append(e['AutoCrossedDefensePC'])
        sums['AutoCrossedDefenseCDF'].append(e['AutoCrossedDefenseCDF'])
        sums['AutoCrossedDefenseMT'].append(e['AutoCrossedDefenseMT'])
        sums['AutoCrossedDefenseRPT'].append(e['AutoCrossedDefenseRPT'])

        if i < 3:
            lastThree['AutoCrossedDefensePC'] += e['AutoCrossedDefensePC']
            lastThree['AutoCrossedDefenseCDF'] += e['AutoCrossedDefenseCDF']
            lastThree['AutoCrossedDefenseMT'] += e['AutoCrossedDefenseMT']
            lastThree['AutoCrossedDefenseRPT'] += e['AutoCrossedDefenseRPT']
            lastThreeCount += 1

    #If there is data, average out the last 3 or less matches
    if (lastThreeCount):
        for key, val in lastThree.items():
            lastThree[key] = round(val / lastThreeCount, 2)

    #If there were matches where the team didn't play D, average those out
    if (noDCount):
        for key, val in noDefense.items():
            noDefense[key] = round(val / noDCount, 2)

    average = dict(AVERAGE_FIELDS)
    median = dict(AVERAGE_FIELDS)
    maxes = dict(AVERAGE_FIELDS)
    for key in sums:
        if key != 'team' and key != 'apr':
            average[key] = round(np.mean(sums[key]), 2)
            median[key] = round(np.median(sums[key]), 2)
            maxes[key] = round(np.max(sums[key]), 2)
    retVal = {
        'averages': average,
        'median': median,
        'maxes': maxes,
        'noDefense': noDefense,
        'lastThree': lastThree
    }

    #Calculate APRs. This is an approximate average points contribution to the match
    for key in retVal:
        apr = 100
#        apr = retVal[key]['autoballs'] + retVal[key]['teleopballs'] + retVal[key]['end']
#        if retVal[key]['autogear']:
#            apr += 20 * min(retVal[key]['autogear'], 1)
#        if retVal[key]['autogear'] > 1:
#            apr += (retVal[key]['autogear'] - 1) * 10
#
#            min(retVal[key]['teleopgear'], 2 - retVal[key]['autogear']) * 20,
#            0)
#        if retVal[key]['autogear'] + retVal[key]['teleopgear'] > 2:
#            apr += min(retVal[key]['teleopgear'] + retVal[key]['autogear'] - 2,
#                       4) * 10
#        if retVal[key]['autogear'] + retVal[key]['teleopgear'] > 6:
#            apr += min(retVal[key]['teleopgear'] + retVal[key]['autogear'] - 6,
#                       6) * 7
        apr = int(apr)
        retVal[key]['apr'] = apr

    return retVal
