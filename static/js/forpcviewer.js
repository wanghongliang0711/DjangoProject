$(function(){
     var i =0;
     var chart = Highcharts.chart('contain', {
                            title: {
                                text: '行程点'
                            },
                            subtitle: {
                                text: 'Show Info of trip'
                            },
                            chart: {
                                backgroundColor: '#DCDCDC',
                            },
                            xAxis:{
                               categories:tm,
                               scrollbar: {
                                    enabled: true
                               },labels: {
                                     style :{
                                        width:'55px',
                                        textOverflow:'ellipsis'
                                    }
                               },
                               tickPixelInterval:null
                            },
                            yAxis: [{
                                title: {
                                    text: '--图像--',
                                },
                                tickPositions: [-1,0,1],
                            },{
                                title:{
                                    text :'--速度--',
                                },
                                tickPositions: [0,90,180],
                                labels: {
                                     format: '{value} km/h',
                                },
                                opposite:true
                            }],
                            legend: {
                                  layout: 'vertical',
                                  align: 'right',
                                  verticalAlign: 'middle',
                                  borderWidth: 0
                            },
                            series:[{
                                name: 'gsensor',
                                data: gsensor,
                                yAxis:0,
                                tooltip: {
                                    valueSuffix: ' G'
                                }
                            }, {
                                name: 'speed',
                                data: speed,
                                yAxis:1,
                                tooltip: {
                                    valueSuffix: ' km/h'
                                }
                            }],
                        });

    $(window).load(function(){  //load状态界面
	    $("#loading").hide();
	});

});