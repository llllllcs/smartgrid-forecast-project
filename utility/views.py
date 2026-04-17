from django.shortcuts import render
from django.views import View
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.conf import settings
from django.template import loader
import json
from rest_framework.views import APIView

import charts
from charts import no

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("{}/templates".format(settings.BASE_DIR)))
REMOTE_HOST = "https://pyecharts.github.io/assets/js"

from django.http import HttpResponse
from pyecharts import options as opts
from pyecharts.charts import Line, Bar, Pie
from pyecharts.globals import ThemeType

# 图表的布局, Page垂直布局，Grid水平布局
from pyecharts.charts import Page, Grid

def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def draw_pie_wait_2():
    car = ["1", "2", "3", "4", "5", "6", "7", "8"]
    num = [19.7, 26.8, 19.5, 2.7, 95.0, 92.6, 109.4, 35.1]
    pie = Pie(init_opts=opts.InitOpts(width="300px", height="360px"))
    pie.add("", [list(z) for z in zip(car, num)], radius=["40%", "75%"], center=["62%", "55%"])
    pie.set_colors(["#5664d2", "#1cbb8c", "#fcb92c", "#ff3d60", "#4aa3ff", "#343a40", "#f06292", "#8d6e63"])
    pie.set_global_opts(title_opts=opts.TitleOpts(is_show=False),
                        legend_opts=opts.LegendOpts(orient="vertical", pos_top="0%", pos_left="2%", legend_icon="pin"))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{d}%', position='inside'))

    grid = Grid(init_opts=opts.InitOpts(width="300px", height="360px"))
    # 设置距离 bar为x轴标签过长的柱状图
    grid.add(pie, grid_opts=opts.GridOpts(pos_top="3%", pos_bottom="10%"))
    # grid.render("templates/pages/utility/mycharts_9.html")
    d = grid.dump_options_with_quotes()
    return d


def pie_base():
    car = ["1", "2", "3", "4", "5", "6", "7", "8"]
    num = [19.7, 26.8, 19.5, 2.7, 95.0, 92.6, 109.4, 35.1]
    c = (
        Pie(init_opts=opts.InitOpts(width="100%", height="360px"))
        .add("", [list(z) for z in zip(car, num)], radius=["40%", "75%"], center=["62%", "55%"])
        .set_colors(["#5664d2", "#1cbb8c", "#fcb92c", "#ff3d60", "#4aa3ff", "#343a40", "#f06292", "#8d6e63"])
        .set_global_opts(title_opts=opts.TitleOpts(is_show=False),
                         legend_opts = opts.LegendOpts(orient="vertical", pos_top="0%", pos_left="2%", legend_icon="pin"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{d}%', position='inside'))
        .dump_options_with_quotes()
    )
    return c


def draw_bar_wait_simultaneous():
    # 设置主题的样式
    bar = Bar(init_opts=opts.InitOpts(width="100%", height="280px"))
    bar.add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8"])
    bar.add_yaxis("新方案", [19.7, 26.8, 19.5, 2.7, 95.0, 92.6, 109.4, 35.1], category_gap="75%", color="#5664d2")

    line = Line(init_opts=opts.InitOpts(width="720px", height="280px"))
    line.add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8"])
    line.add_yaxis("新方案", [19.7, 26.8, 19.5, 2.7, 95.0, 92.6, 109.4, 35.1], is_smooth=True, symbol="emptyCircle", symbol_size=0, linestyle_opts=opts.LineStyleOpts(color='#1cbb8c', width=2))
    line.set_global_opts(
        title_opts=opts.TitleOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    # 增加主题和副标题
    bar.set_global_opts(
        title_opts=opts.TitleOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(name="叉车编号", name_location='center', name_gap=15, splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(name="时间/min", name_location='center', name_gap=30, splitline_opts=opts.SplitLineOpts(is_show=False)),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[
        #         opts.MarkPointItem(type_="max", name="最大值")], symbol_size=50),
        itemstyle_opts={"normal": {"barBorderRadius": [5, 5, 0, 0]}},
    )
    grid = Grid(init_opts=opts.InitOpts(width="720px", height="280px"))
    # 设置距离 bar为x轴标签过长的柱状图
    grid.add(bar, grid_opts=opts.GridOpts(pos_top="3%", pos_bottom="10%"))
    grid.add(line, grid_opts=opts.GridOpts(pos_top="3%", pos_bottom="10%"))
    # grid.render("templates/pages/utility/mycharts_8.html")
    c = grid.dump_options_with_quotes()
    return c


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.draw_pie_wait_2()))


class ChartView_2(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.draw_bar_wait_simultaneous()))


class MapView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.draw_map()))


def heatmap(request):
    return render(request, 'pages/utility/mycharts_heat.html', {})


class TextView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.collision_deadlock_num()))


class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.task_simultaneous()))


class LocView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.loc_simultaneous()))


class WaitNumView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.wait_car_simultaneous()))


class ProcessView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.process_simultaneous()))


class MoveView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(charts.move_simultaneous()))

# number = 0



# Starter Page
class StarterPageView(APIView):
    def get(self, request, *args, **kwargs):
        # global number
        templates = loader.get_template('menu/index-2.html')
        greeting = {}
        greeting['title'] = "实时监控看板"
        greeting['pageview'] = "运行过程监控"
        greeting['collision'] = str(charts.list_collision[no])
        print(no)
        return HttpResponse(templates.render(greeting, request))

# Maintenance
class MaintenanceView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "可视化场景监控"
        greeting['pageview'] = "运行过程监控"
        return render(request,'pages/utility/pages-starter.html',greeting)
        
# Coming-Soon
class ComingSoonView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "实时场景监控"
        greeting['pageview'] = "可视化"
        return render(request,'pages/utility/pages-starter.html',greeting)

# Timeline
class TimelineView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "Timeline"
        greeting['pageview'] = "Utility"
        return render(request,'pages/utility/pages-timeline.html',greeting)

# Faqs
class FaqsView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "FAQs"
        greeting['pageview'] = "Utility"
        return render(request,'pages/utility/pages-faqs.html',greeting)

# Pricing
class PricingView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "Pricing"
        greeting['pageview'] = "Utility"
        return render(request,'pages/utility/pages-pricing.html',greeting)

# Error 404
class Error404View(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "Error 404"
        greeting['pageview'] = "Utility"
        return render(request,'pages/utility/pages-404.html',greeting)

# Error 500
class Error500View(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "Error 500"
        greeting['pageview'] = "Utility"
        return render(request,'pages/utility/pages-500.html',greeting)


class TestView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "离线仿真验证"
        greeting['pageview'] = "结果展示"
        return render(request,'pages/utility/pages-starter-test.html',greeting)


"""def draw_bar(request):
    # 设置主题的样式
    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [5, 20, 36, 10, 60, 100])
    bar.add_yaxis("商家B", [3, 15, 32, 20, 75, 60])
    # 增加主题和副标题
    bar.set_global_opts(title_opts=opts.TitleOpts(title="主题", subtitle="副标题"))
    bar.render("%s/templates/mycharts.html" % settings.BASE_DIR)
    return render(request, "mycharts.html")"""


def jump_bars(request):
    return render(request, 'pages/utility/mycharts.html', {})


def compare_bars(request):
    return render(request, 'pages/utility/mycharts_2.html', {})


def wait_bars(request):
    return render(request, 'pages/utility/mycharts_3.html', {})


def analysis_bars_time(request):
    return render(request, 'pages/utility/mycharts_4.html', {})


def analysis_bars_wait(request):
    return render(request, 'pages/utility/mycharts_5.html', {})


# def line_collision(request):
#     return render(request, 'pages/utility/mycharts_6.html', {})


def pie_wait(request):
    return render(request, 'pages/utility/mycharts_7.html', {})


def bar_wait_simultaneous(request):
    return render(request, 'pages/utility/mycharts_8.html', {})


def pie_wait_2(request):
    return render(request, 'pages/utility/mycharts_9.html', {})

"""def index(request):
    # pyecharts 支持链式调用
    # // 设置行名
    columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # // 设置数据
    data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

    """"""初始化时Page()中是可以指定参数的，比如layout，DraggablePageLayout是令每个模块可以被任意拖动、
    缩放，便于人工布局；SimplePageLayout是令每个模块自动水平居中对齐。不指定的话，所有模块就会靠左对齐。""""""
    page_1 = Page(layout=Page.SimplePageLayout)
    # 初始化grid对象
    grid1_1 = Grid(init_opts=opts.InitOpts(theme=ThemeType.ROMA, width='1600px'))

    # 折线图
    line = (
        # 创建折线图
        Line()
        # 增加主标题与副标题
        .set_global_opts(title_opts=opts.TitleOpts(title="折线图", subtitle="一年的降水量与蒸发量"))
        # X轴标签
        .add_xaxis(columns)
        # 增加折线图数据, symbol_size:圆点的大小，is_smooth:是否圆滑曲线,color:曲线的颜色
        # 注意：当上面的init_opts设置了主题样式后，color就不起作用了
        .add_yaxis("降水量", data1, symbol_size=10, is_smooth=True, color="green",
                   markpoint_opts=opts.MarkPointOpts(data=[
                       opts.MarkPointItem(name="最大值", type_="max"),
                       opts.MarkPointItem(name="最小值", type_="min")]))
        .add_yaxis("蒸发量", data2, symbol_size=10, is_smooth=True, color="blue")
    )

    # 柱状图
    # 创建柱状图
    bar = Bar()
    # 增加主题和副标题
    bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图", subtitle="一年的降水量与蒸发量"))
    # 添加柱状图的数据
    bar.add_xaxis(columns)
    bar.add_yaxis("降水量", data1)
    bar.add_yaxis("蒸发量", data2)
    # 增加平均线
    bar.set_series_opts(markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="平均值", type_="average")]))
    # 增加最大值,最小值
    bar.set_series_opts(markpoint_opts=opts.MarkPointOpts(data=[
        opts.MarkPointItem(name="最大值", type_="max"),
        opts.MarkPointItem(name="最小值", type_="min")
    ]))

    # 将两个图表分别添加到grid对象里面去
    # 对grid的pos参数而言，pos_left是显示在靠右的位置 pos_right同理
    grid1_1.add(line, grid_opts=opts.GridOpts(pos_right="55%"))
    grid1_1.add(bar, grid_opts=opts.GridOpts(pos_left="55%"))
    # page里可以add多种元素，grid chart image等等
    page_1.add(grid1_1)
    return HttpResponse(page_1.render_embed())


def show_pyecharts(request):
    bar = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    )
    bar.render("%s/templates/pages/utility/pages-starter-test.html" % settings.BASE_DIR)
    # print(bar.render_embed())
    # print(bar.dump_options())
    return render(request, 'pages/utility/pages-starter-test.html')



class TestView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "图表"
        greeting['pageview'] = "测试"
        return render(request,'pages/utility/pages-starter-test.html',greeting)

    def show_pyecharts(self, request):
        bar = (
            Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        )
        bar.render("%s/templates/pages/utility/pages-starter-test.html" % settings.BASE_DIR)
        # print(bar.render_embed())
        # print(bar.dump_options())
        return render(request, 'pages/utility/pages-starter-test.html')"""


class SimulationView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "运行过程仿真"
        greeting['pageview'] = "控制方案验证"
        return render(request, 'pages/utility/simulation.html', greeting)


def result_page(request):
    template = loader.get_template('pages/utility/pages-starter-test.html')
    p_1 = charts.draw_bar_compare()
    p_2 = charts.draw_pie_wait()
    p_3 = charts.draw_bar_time()
    p_4 = charts.draw_bar_wait()
    p_5 = charts.draw_bar_analysis_time()
    p_6 = charts.draw_bar_analysis_wait()
    context = dict(
        myechart_1=p_1.render_embed(),
        myechart_2=p_2.render_embed(),
        myechart_3=p_3.render_embed(),
        myechart_4=p_4.render_embed(),
        myechart_5=p_5.render_embed(),
        myechart_6=p_6.render_embed(),
        host=REMOTE_HOST,
        script_list_1=p_1.js_dependencies.items,
        script_list_2=p_2.js_dependencies.items,
        script_list_3=p_3.js_dependencies.items,
        script_list_4=p_4.js_dependencies.items,
        script_list_5=p_5.js_dependencies.items,
        script_list_6=p_6.js_dependencies.items,
        title='验证结果展示',
        pageview='控制方案验证'
    )
    return HttpResponse(template.render(context, request))


def starter_page(request):
    template = loader.get_template('menu/index-2.html')
    greeting = {}
    greeting['title'] = "实时数据监控"
    greeting['pageview'] = "运行过程监控"
    return render(request, 'menu/index-2.html', greeting)