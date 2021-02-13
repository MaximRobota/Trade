import random

limit = 20
trend = 1000
n = 0.01
data = []
historyData = []
historyBayData = []
dataSeries = { type: "line" }
historyDataSeries = { type: "line" }
historyBayDataSeries = { type: "line" }
dataPoints = []
historySellPoints = []
historyBayPoints = []
maxAmountFails = 0
player1 = {
    'name': 'player1',
    'money': 1000,
    'position': [],
    'history': []
}
player2 = {
    'name': 'player2',
    'money': 1000,
    'position': [],
    'history': []
}
player3 = {
    'name': 'player3',
    'money': 1000,
    'position': [],
    'history': [{
        'price': 1000,
        'trend': trend,
    }]
}

def random_number(min, max):
    return random.randint(min, max)


for i in limit:
    if (i > 0) :
        # trend = trend + 10
        trend += random_number(-1, 2) * n


    player1_choose_position(trend, i);
    player2_choose_position(trend, i);
    player3_choose_osition(trend, i);

    dataPoints.push({
        'x': i,
        'y': trend
    })

    if (i === limit - 1):
        sellBTC(trend, player1);
        sellBTC(trend, player2);
        sellBTC(trend, player3);
        sellUSDT(trend, player1);
        sellUSDT(trend, player2);
        sellUSDT(trend, player3);
        console.log(player3.history);

        var lowest = Number.POSITIVE_INFINITY;
        var highest = Number.NEGATIVE_INFINITY;
        var tmp;
        for (var k=player3.history.length-1; k>=0; k--) {
            tmp = player3.history[k].price;
            if (tmp < lowest) lowest = tmp;
            if (tmp > highest) highest = tmp;
        }
        console.log(highest, lowest);