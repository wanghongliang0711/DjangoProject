
$(function(){
     $('.cl').click(function f1(){
<!--           分页显示table数据-->
           nuit_id = $(this).text().substring(2,)
           $.ajax({
                'url':'show11',
                'type':'get',
                'data':nuit_id,
                'success':function(rst){
                   data = JSON.parse(rst['context']);
                   $("tbody").html('');
                   for(var i in data){
                        $("tbody").append('<tr><td>'+data[i].metadata_positioning_data_positioning_time+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_quality+'</td><td>'+data[i].metadata_positioning_data_velocity+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_positioning_status+'</td></tr>')
                                      }
                $('#pagespan').html(1)
                    }
                })

<!--            提取所有数据显示折线图-->
            var ptime = [];
            var quality = [];
            var velocity = [];
            var status = [];
            var index = 0;
            var hx = 0;
            $.ajax({
                'url':'show',
                'type':'get',
                'data': nuit_id,
                'success':function(data){
<!--                    $("tbody").html('');-->
                    for(var i in data){
                       ptime.push(data[i].metadata_positioning_data_positioning_time.substring(9,18))
                       quality.push(data[i].metadata_positioning_data_quality)
                       velocity.push(data[i].metadata_positioning_data_velocity)
                       status.push(data[i].metadata_positioning_data_positioning_status)
                       index+=1;
                        }
                $('#sp').html(nuit_id+'共'+index+'条数据');
<!--                开始画图用highcharts技术-->

                var chart = Highcharts.chart('hct', {
                            title: {
                                text: '行程点'
                            },
                            subtitle: {
                                text: 'Show Info of trip'
                            },
                            chart: {
                                zoomType: 'x'
                            },
                            xAxis:{
                               categories:ptime,
                               scrollbar: {
                                    enabled: true
                               },
                               labels: {
                                     style :{
                                        width:'55px',
                                        textOverflow:'ellipsis'
                                    }
                               }
                            },
                            yAxis: {
                                title: {
                                    text: '--Trip State--'
                                },
                                plotLines: [{
                                 value: -50,
                                 width: 1,
                                 color: '#804125'
                              }]
                            },
                            legend: {
                                  layout: 'vertical',
                                  align: 'right',
                                  verticalAlign: 'middle',
                                  borderWidth: 0
                            },
                            plotOptions: {
                                series: {
                                    events:{
                                        click:function(e){
                                           hx = chart.xAxis[0].categories.indexOf(e.point.category);
                                           $.ajax({
                                                 "url":"show13",
                                                 "data": {'nuit_id':nuit_id,'time':e.point.category},
                                                 "success":function(rst){
                                                     console.log(typeof(rst));
                                                     data = JSON.parse(rst['data']);
                                                     $("tbody").html('');
                                                     for(var i in data){
                                                         $("tbody").append('<tr><td>'+data[i].metadata_positioning_data_positioning_time+'</td>'+
                                                         '<td>'+data[i].metadata_positioning_data_quality+'</td><td>'+data[i].metadata_positioning_data_velocity+'</td>'+
                                                         '<td>'+data[i].metadata_positioning_data_positioning_status+'</td></tr>')
                                                         }
                                                     }
                                                 });
                                           i++;
                                           chart.xAxis[0].addPlotLine({
                                                value:hx,
                                                width:2,
                                                color: 'red',
                                                id: 'plot-line-'+i+''
		                                    });
                                        }
                                    },
                                    label: {
                                        connectorAllowed: false
                                    }
                                }
                            },
                            plotLines:{
                                 events:{
                                    mouseover:function(){
                                        return '标示线';
                                     }
                                 }
                            },
                            series:[{
                                name: 'velocity',
                                data: velocity
                            }, {
                                name: 'status',
                                data: status
                            },  {
                                name: 'quality',
                                data: quality
                            }],
                        });
                $('#hct').append("<button class='remove'>删标识线</button>")
                $(".remove").click(function(){
                        if(i>0) {
                            chart.xAxis[0].removePlotLine("plot-line-"+i+'');
                            i--;
                                 }
	                    })


                }
            })
      });

    $('#next').click(function(){
        var page = $('#pagespan').text();
        var nuitid = $('#sp').text().substring(0,11);
        page++;
        $.ajax({
            'url':'show12',
            'type':'get',
            'data':{'page':page,'nuit_id':nuitid},
            'success':function(rst){
                   data = JSON.parse(rst['context']);
                   $("tbody").html('');
                   for(var i in data){
                        $("tbody").append('<tr><td>'+data[i].metadata_positioning_data_positioning_time+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_quality+'</td><td>'+data[i].metadata_positioning_data_velocity+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_positioning_status+'</td></tr>')
                                      }
            $('#pagespan').html(rst['page'])
            if(Object.keys(rst).length==3){$('#next').hide();}
            else{$('#next').show();}
                    }
              })
     });

     $('#pre').click(function(){
        var page = $('pagespan').text();
        var nuitid = $('#sp').text().substring(0,11);
        if(page!=1){page--;}
        $.ajax({
            'url':'show12',
            'type':'get',
            'data':{'page':page,'nuit_id':nuitid},
            'success':function(rst){
                   data = JSON.parse(rst['context']);
                   $("tbody").html('');
                   for(var i in data){
                        $("tbody").append('<tr><td>'+data[i].metadata_positioning_data_positioning_time+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_quality+'</td><td>'+data[i].metadata_positioning_data_velocity+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_positioning_status+'</td></tr>')
                                      }
            $('#pagespan').html(rst['page'])
            if(rst['page']<=1){ $('#pre').hide();}
            else{$('#pre').show();}
                    }
              })
     });

     $('#first').click(function(){
        var nuitid = $('#sp').text().substring(0,11);
        $.ajax({
            'url':'show12',
            'type':'get',
            'data':{'page':1,'nuit_id':nuitid},
            'success':function(rst){
                   data = JSON.parse(rst['context']);
                   $("tbody").html('');
                   for(var i in data){
                        $("tbody").append('<tr><td>'+data[i].metadata_positioning_data_positioning_time+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_quality+'</td><td>'+data[i].metadata_positioning_data_velocity+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_positioning_status+'</td></tr>')
                                      }
            $('#pagespan').html(1);
                    }
              })
      });

      $('#last').click(function(){
         var nuitid = $('#sp').text().substring(0,11);
         $.ajax({
            'url':'show12',
            'type':'get',
            'data':{'page':-1,'nuit_id':nuitid},
            'success':function(rst){
                   data = JSON.parse(rst['context']);
                   $("tbody").html('');
                   for(var i in data){
                        $("tbody").append('<tr><td>'+data[i].metadata_positioning_data_positioning_time+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_quality+'</td><td>'+data[i].metadata_positioning_data_velocity+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_positioning_status+'</td></tr>')
                                      }
            $('#pagespan').html(rst['totalpage']);
                    }
              })
      });

      $('select').change(function(){
           var select = $(this).val();
           var nuitid = $('#sp').text().substring(0,11);
           $.ajax({
            'url':'show12',
            'type':'get',
            'data':{'select':select,'nuit_id':nuitid},
            'success':function(rst){
                   data = JSON.parse(rst['context']);
                   $("tbody").html('');
                   for(var i in data){
                        $("tbody").append('<tr><td>'+data[i].metadata_positioning_data_positioning_time+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_quality+'</td><td>'+data[i].metadata_positioning_data_velocity+'</td>'+
                        '<td>'+data[i].metadata_positioning_data_positioning_status+'</td></tr>')
                                      }
            $('#pagespan').html(1);
                    }
              })
      });
 });

    $(window).load(function(){  //load状态界面
			$("#loading").hide();
		});
