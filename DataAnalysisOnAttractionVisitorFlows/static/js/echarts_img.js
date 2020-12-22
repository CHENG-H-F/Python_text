var option_compare = {
    title: {
        text: "Multl-attraction Data Comparison",
        left: 'center',
        itemGap: 10,
        subtextStyle: {
            left: 'center',
            align: 'center',
            fontFamily: 'Arial',
            fontSize: 14,
        }
    },
    tooltip: {
        trigger: 'axis'
    },
    toolbox: {
        show: true,
        feature: {
            magicType: {show: true, type: ['stack', 'tiled']},
            saveAsImage: {show: true}
        }
    },
    dataZoom: [{
        start: 60,
        end: 100,
    }, {
        type: 'inside'
    }],
    legend: {
        x: 'center',
        y: 'bottom',
        data: ''
    },
    xAxis: {
        boundaryGap: false,
        type: 'category',
        name: 'Time',
        nameLocation: 'end',
        nameGap: 25,
        data: '',
        textStyle: {
            fontSize: 18,
            fontFamily: 'Arial'
        }
    },
    yAxis: {
        type: 'value',
        name: 'Visitor flow',
        nameLocation: 'middle',
        nameGap: 55,
        textStyle: {
            fontSize: 18,
            fontFamily: 'Arial'
        }
    },
    series: ''
};

function getDateSingle(name, subtext, myChart) {
    $.ajax({
        type: "POST",
        url: "search/",
        data: {name: name},
        dataType: 'json',
        success: function (data) {
            console.log(data);
            single_echart(data, name, myChart, subtext, true);
        },
        error: function (data) {
            console.log("error!");
        }
    });
}

// data为ajax返回的数据，name为景点名称，subtext为副标题，boolean用来指定是否开启动画和是否显示echarts。
function single_echart(data, name, myChart, subtext, booblen) {
    myChart.setOption({
        show: booblen,
        title: {
            text: name,
            left: 'center',
            itemGap: 10,
            subtext: subtext,
            subtextStyle: {
                left: 'center',
                align: 'center',
                fontFamily: 'Arial',
                fontSize: 14,
            }
        },
        tooltip: {
            trigger: 'axis'
        },
        toolbox: {
            show: true,
            feature: {
                magicType: {show: true, type: ['stack', 'tiled']},
                saveAsImage: {show: true}
            }
        },
        dataZoom: [{
            start: 60,
            end: 100,
        }, {
            type: 'inside'
        }],
        legend: {
            x: 'center',
            y: 'bottom',
            data: ['Visitor flow'],

        },
        xAxis: {
            name: 'Time',
            nameLocation: 'end',
            nameGap: 35,
            type: 'category',
            data: data.time,
            textStyle: {
                fontSize: 18,
                fontFamily: 'Arial',
            }
        },
        yAxis: {
            name: 'Visitor flow',
            nameLocation: 'middle',
            nameGap: 55,
            type: 'value',
            textStyle: {
                fontSize: 18,
                fontFamily: 'Arial',
            }

        },
        series: [{
            name: 'visitor flow',
            data: data.num,
            type: 'line',
            markLine: {
                data: [{type: 'max', name: 'max'}, {type: 'min', name: 'min'}]
            },
        }],
        animation: booblen,
    }, true);
    var picInfo = myChart.getDataURL();
    create_img(picInfo, name);
}

function getDateCompare(names, subtext, myChart) {
    $.ajax({
        type: "POST",
        url: "compare/",
        data: {names},
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log(data);
                option_compare.legend.data = data.name;
                option_compare.series = data.series;
                option_compare.xAxis.data = data.date;
                option_compare.title.subtext = subtext;
                // 加入true，每次点击之后自动刷新
                myChart.setOption(option_compare, true);
            } else {
                alert("You haven't chosen a scenic spot yet!")
            }
        },
        error: function () {
            console.log("error!")
        }
    });
}

function getDateReportCompare(names, subtext, myChart) {
    $.ajax({
        type: "POST",
        url: "report/",
        data: {names: names},
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log(data.series)
                option_compare.legend.data = data.name;
                option_compare.series = data.series;
                option_compare.xAxis.data = data.date;
                option_compare.animation = false;
                option_compare.title.subtext = subtext;
                myChart.clear();
                myChart.setOption(option_compare, true);
                var picInfo = myChart.getDataURL();
                create_img(picInfo, "Chart with mutiple spot data");
            } else {
                alert("You have not selected the attractions to generate the report!")
            }
        },
        error: function () {
            console.log("error!")
        }
    });
}

function getDateReportSingle(name, subtext, myChart) {
    $.ajax({
        type: "POST",
        url: "search/",
        data: {name: name},
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log(data);
                myChart.clear();
                single_echart(data, name, myChart, subtext, false);
            } else {
                alert("You have not selected the attractions to generate the report!")
            }

        },
        error: function (data) {
            console.log("error!");
        }
    });
}

function create_img(picInfo, name) {
    $.ajax({
        type: "POST",
        url: "create_img/",
        data: {'picInfo': picInfo, 'name': name},
        dataType: 'json',
        success: function (response, status, request) {
            if (response === 1) {
                console.log("Image generated successfully!")
            }
            if (response === 2) {
                $("#input_dow").show();
            }
            if (response === 0) {
                alert("Failed to generate image!");
            }
        },
        error: function () {
            console.log("error!");
        }
    });
}

