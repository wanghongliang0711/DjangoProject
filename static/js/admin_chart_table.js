$(function(){
     var i =0;		// 一会儿添加标示线用的，因为删标示线时要根据索引
     var chart = Highcharts.chart('contain', {
                            title: {
                                text: 'admin主标题'				// 主标题
                            },
                            subtitle: {
                                text: 'admin副标题'	// 副标题
                            },
                            chart: {
                                zoomType: 'x'	// 可以沿x轴放大，用鼠标拖动一段距离  'xy'  'x' 'y'
                            },
                            xAxis:{
                               categories:pt,	// 横轴显示什么数据pt
                               scrollbar: {
                                    enabled: true		// scrollbar加个滚动块
                               },labels: {
                                     style :{
                                        width:'70px',			// 时间显示 多长后隐藏
                                        textOverflow:'ellipsis'	  // x轴上字段内容太长最后用..代替
                                    }
                               },
                               tickPixelInterval:null		// x轴刻度间的间距px,null就自适应
                            },
                            yAxis: {
                                title: {
                                    text: '--admin y 轴 标 题 --'		// y轴标题
                                },
                                plotLines: [{
                                 value: 8,			// 最低的y轴的值
                                 width: 3,				// 那一条横线的宽度
                                 color: '#804125'		// 那一条横线的颜色
                              }]
                            },
                            legend: {  // 图例说明是包含图表中数列标志和名称的容器
                                  layout: 'vertical',	// 每条线的标头垂直显示、horizontal水平
                                  align: 'right',		// 左中右
                                  verticalAlign: 'middle',		// 上中下
                                  borderWidth: 0		// 无边框
                            },
                            plotOptions: {		// 增删标示线的函数
                                series: {		// 固定写法
                                    events:{		// 动态函数
                                        click:function(e){		// 点击highchart里的图时触发
                                           // chart.xAxis[0].categories   获取所有所有的 X 轴坐标数据
                                           // e.point.category 被点击的 点 的坐标值
                                           // chart.xAxis[0].categories.indexOf(e.point.category)  点击的是点几个点 从0开始算
                                           hx = chart.xAxis[0].categories.indexOf(e.point.category);	// 获取点击的是属于x轴上哪个刻度值,索引它是第几个刻度点
                                           nuit_id = '21C100552';
                                           alert('最近点：' + event.point.category + '\n'+
                                           'hx: ' +chart.xAxis[0].categories.indexOf(e.point.category) + '\n'
                                           );
                                           $.ajax({
                                                 "url":"blake_show13",	// 点完后交给show13函数去处理
                                                 "data": {'nuit_id':nuit_id,'time':e.point.category},	// 传给show13的参数,哪辆车,哪一时间
                                                 "success":function(rst){
                                                     mytable.clear();					// datatable清空再画新的
                                                     mytable.rows.add(rst['data']);		// show13返回的数据逐行添加到datatable里
                                                     mytable.columns.adjust().draw();	// 开始画表格

                                                     var chooserow = mytable.rows().eq(0).filter(function(rowIdx){
                                                        return mytable.cell(rowIdx,0).data() === e.point.category ? true:false;
                                                     });								// 找到在highcharts里点的那一点的刻度的数据(时间)

                                                     mytable.row(chooserow).nodes().to$().css('background','lightgreen');	// 这一行数据添加格式背景浅绿色

                                                     var dy = $("tbody").find("tr").eq(0).offset().top;		// 表格第一行距页面顶部多少距离
                                                     var dq = $("tbody").find("tr").eq(mytable.row(chooserow).index()).offset().top;	// 绿的那一行距页面顶部多少距离
                                                     var huadong = dq-dy-$('.odd').height()*6;			// 二者隔多少距离再减去 ‘一个表格的高度乘以6’--(自己调节的随便写)
                                                     $('.dataTables_scrollBody').scrollTop(huadong);	// 表格(tbody是datatable自己取的名)里的滑动块滑到绿的那一行

                                                     if ($('.remove').next().length == 0){
                                                         $('.remove').after('<button>返回所有数据</button>'); // ‘删标示线’按钮后加一个按钮‘返回所有数据’,没此按钮时才加
                                                     }
                                                     $(".remove").next().click(function(){		// ‘返回所有数据’按钮点了会怎样
                                                        mytable.clear();						// datatable内容清空
                                                        mytable.rows.add(data1);				// 再将首次获取的test.html里的全部数据拿到
                                                        mytable.columns.adjust().draw();		// 画上去	
                                                        $(".remove").nextAll().remove();		// ‘删标示线’按钮后的所有内容清空(返回所有数据 按钮)
                                                        });
                                                     }
                                                 });
                                           huaxian(hx);			// 调huaxian函数把索引值传进去在highcharts上画标示线  //**********
                                        },legendItemClick: function () {						// 每条线的标头点击会怎样？此函数是为了记忆上次页面上哪些线是隐藏或是显示的
                                            var visiline = [];									// 加一个存储当前所有可见的线的集合
                                            for(i=0,length=chart.series.length;i<length;i++){	// 开始遍历所有线  chart.series.length  一共几条线，这里是4条
                                                if(chart.series[i].visible){					// 这条线没点击前的状态  遍历到某条线时若该线可见的话
                                                    if(chart.series[i].name!=this.name){		// 再判断该线的名字若不等于被点的线的标头	
                                                        visiline.push(chart.series[i].index);	// 该线的索引值加到列表里
                                                    }
                                                }else{											// 遍历到某条线时若该线不可见的话
                                                    if(chart.series[i].name==this.name){		// 再判断该线的名字若等于被点的线的标头时
                                                    visiline.push(chart.series[i].index);		// 将该线的索引值加到列表里
                                                    }

                                                }
                                            }
                                            alert('最近点：' + visiline + '\n'+'chart.series.length:' +  chart.series.length+'\n')
                                        }

                                    },

                                    label: {
                                        connectorAllowed: false		// ？？
                                    }
                                }
                            },
//                            plotLines:{
//                                 events:{
//                                    mouseover:function(){
//                                        return '标示线';			// ？？
//                                     }
//                                 }
//                            },
                            series:[{
                                name: 'gsq',
                                data: gsq						// 每条线显示的数据
                            }, {
                                name: 'vel',
                                data: vel,
                                visible: false
                            },  {
                                name: 'lat',
                                data: lat
                            },{
                                name: 'satellite_num',
                                data: satellite_num
                            }],
                        });             <!--   画折现结束   -->
      $('#contain').append("<button class='remove'>删标识线</button>")

      $(".remove").click(function(){
             if(i>0) {					// 若有多个标示线，则按后加(0,1,2..)先删(3,2,1,0)的顺序去删
                  chart.xAxis[0].removePlotLine("plot-line-"+i+'');
                  i--;
             }
       })

     $('#title').append(' --21C100552 行程信息表--');


     var mytable = $('#example').DataTable({		//生成表格对象开始画表格
           scrollY: 420,							// 表格高度超过420像素就显示滑动块
           aLengthMenu:[[20,40], [20,40]],	// 第一个[1800,3600]是表格每页显示1800/3600条数据受第二个控制,第二个表格下拉框一页显示1800/3600条数据？？
           data: data1,								// 使用哪些数据画表格			
           columns:tablehead,						// 表格的表头是哪些,[{'title':'...'},{},{}]
           ordering:false,		// 不自动排序，会打乱原始顺序
           scrollX: true,		// 滑动块在x轴上
           searching:false,		// 不要搜索框
        });

	 $('.typecheck').change(function(){		// 筛选所需列的函数
	 	 allbiaotou = [];					// 存放所有表头
		 for(var i=0,len=tablehead.length;i<len;i++){
				allbiaotou.push(tablehead[i]['title']);
		 }

         var nochoose = [];
         $("input:checkbox").not("input:checked").each(function(){
               nochoose.push($(this).val());	// 存放所有未被选中的表头
         });
         nochooseindex = [];
         for(var i in nochoose){			    // 存放所有未被选中的表头在allbiaotou里的索引
             nochooseindex.push(allbiaotou.indexOf(nochoose[i]));
         }
         totalindex = [];						// 所有的allbiaotou的索引值,也就是0,1...直至列表长度
         for(var i=0,len=allbiaotou.length;i<len;i++){
            totalindex.push(i);             // /************  push
         }
                                                        // /*********key => !nochooseindex.includes(key))
         chooseindex = totalindex.filter(key => !nochooseindex.includes(key));	// js反向选中被选中的列的索引
         mytable.columns(nochooseindex).visible(false,false);	// 未选中的列的可见性为false不可见
         mytable.columns(chooseindex).visible(true,false);		// 选中的列的可见性为true可见
         mytable.columns.adjust().draw(false);				//  加了false后  翻页后 改变列数，不会自动翻到第一页，还停留在当前页
    });

    $("#select_all").click(function(){			// 筛选所需列里的全选按钮，和全不选按钮
			$('.cb').prop("checked",true);			
			$('.typecheck').trigger('change');
		})

	$("#cancle_all").click(function(){
			$('.cb').prop("checked",false);
			$('.typecheck').trigger('change');
		})

	$('#show,#cbox').mouseover(function(){$('#cbox').show().css('background','#4CAF50');})	// 筛选所需列内容在鼠标悬停时显示,离开时隐藏
	.mouseout(function(){$('#cbox').hide()});

	function huaxian(hx){
            i++;							// 标示线总数加1
            chart.xAxis[0].addPlotLine({
                value:hx,					// 之前拿到的索引值在此点画线
                width:2,					// 标示线的宽度
                color: 'red',				// 标示线的颜色
                id: 'plot-line-'+i+'',		//标示线的id，在删除该标示线的时候需要该id标示
                events:{
                    mouseover:function(){
                        chart.tooltip.shared=true		// 鼠标放到标示线上会显示内容
                    },
                    mouseout:function(){
                        setTimeout(function () {
                                chart.tooltip.shared=false;		//鼠标离开标示线上内容消失在3.7秒内
                                },3700)
                        }
                    }
			});
        };

    $(window).load(function(){  //load状态界面
	    $("#loading").hide();	// 页面没加载完内容时显示#loading的内容，加载完了loading消失显示加载后的内容

		$("#example").delegate('tr','click', function () {				// 表格对象里的某一行被点击时触发的函数
           if($(this).css('background-color')=='rgb(144, 238, 144)'){	// 若该行是浅绿色(就是点标示线时单独被拎出来了)
					$(this).css('background','rgb(255, 255, 255)')		// 去除该行浅绿色的背景
					$(".remove").trigger("click");						// 让‘删标示线’按钮点击，删掉该标示线
				}else{
					$(this).css('background','#90ee90');				// 若该行不是浅绿色就变为浅绿色
<!--					然后找到折线图上的点画线-->
                    pointindex = mytable.row(this).index();				// 索引该行在数据内容中的索引值
                    huaxian(pointindex);								// 根据索引值去highcharts图上画标示线
<!--                    折线图上滚动条滑动至该点-->
                    var startpindex = pointindex-100>0?pointindex-100:0;    // /**************
                    var endpindex = pointindex+100>(pt.length)?(pt.length):pointindex+100;
                    chart.xAxis[0].setExtremes(startpindex,endpindex);
				}
        });
	});

});