#%%
from pyecharts.charts import Bar, Grid, Pie, Line, HeatMap
from django.conf import settings
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import pandas as pd
import numpy as np
import json as js

df_total = pd.read_csv('D:/ieee/Admin/info.csv', na_values='无')
df_wait = df_total[['wait_1', 'wait_2', 'wait_3', 'wait_4', 'wait_5', 'wait_6', 'wait_7', 'wait_8']].copy()
df_loc = df_total[['loc_1', 'loc_2', 'loc_3', 'loc_4', 'loc_5', 'loc_6', 'loc_7', 'loc_8']].copy()
# df_task = df_total[['task_1', 'task_2', 'task_3', 'task_4', 'task_5', 'task_6', 'task_7', 'task_8']].copy()
df_process = df_total[['process_1', 'process_2', 'process_3', 'process_4',
                       'process_5', 'process_6', 'process_7', 'process_8']].copy()
# df_task = df_task.fillna(0)
# df_task = df_task.astype(int)
# for i in range(df_task.shape[0]):
#     for j in range(8):
#         if df_task.iloc[i, j] < 0:
#             df_task.iloc[i, j] = -1

# df_task = df_task.astype(str)

# for i in range(df_task.shape[0]):
#     for j in range(8):
#        if df_task.iloc[i, j] == '0':
#            df_task.iloc[i, j] = '当前无任务'
#         if df_task.iloc[i, j] == '-1':
#             df_task.iloc[i, j] = '返回任务'

# df_task.to_csv('C:/Users/XN/PycharmProjects/Nazox/Admin/info_task.csv', index=False, encoding='utf_8_sig')

df_task = pd.read_csv('D:/ieee/Admin/info_task.csv', encoding='utf_8_sig')

list_collision = list(df_total['collision'])
list_deadlock = list(df_total['deadlock'])
arr_wait = np.array(df_wait).astype(float)
arr_loc = np.array(df_loc).astype(str)
arr_task = np.array(df_task).astype(str)
arr_process = np.array(df_process).astype(float)
arr_loc_int = np.array(df_loc).astype(int)

'''df_map = pd.read_csv('D:/ieee/Admin/map.csv')
value = np.zeros((45, 158), dtype=int)
for i in range(df_map.shape[0]):
    value[df_map.iloc[i, 2] - 1][df_map.iloc[i, 1] - 1] = df_map.iloc[i, 3]

data_map = []
for h in range(0, 158):
    for w in range(0, 45):
        data_map.append([h, w, value[w][h]])

map_x_axis = []
for i in range(1, 159):
    map_x_axis.append(str(i))
map_y_axis = []
for i in range(1, 46):
    map_y_axis.append(str(i))'''


no = 0


def collision_deadlock_num():
    list_collision_deadlock = []
    list_collision_deadlock.append(list_collision[no])
    list_collision_deadlock.append(list_deadlock[no])
    wait_max = np.around(np.max(arr_wait[no]) / 60, 2)
    list_collision_deadlock.append(wait_max)
    wait_average = np.around(np.mean(arr_wait[no]) / 60, 2)
    list_collision_deadlock.append(wait_average)
    max_index = str(np.argmax(arr_wait[no]) + 1)
    list_collision_deadlock.append(max_index)
    print(no)
    return json.dumps(list_collision_deadlock)


def task_simultaneous():
    return json.dumps(list(arr_task[no]))


def loc_simultaneous():
    return json.dumps(list(arr_loc[no]))


def process_simultaneous():
    return json.dumps(list(np.around(arr_process[no] * 100)))


def move_simultaneous():
    arr_temp = arr_wait[no].copy()
    list_move = [100 - 50 * x / (no + 1) for x in arr_temp]
    arr_move = np.around(np.array(list_move), 2)
    return json.dumps(list(arr_move))


def wait_car_simultaneous():
    list_wait = []
    for i in range(8):
        if arr_wait[no][i] != arr_wait[no - 1][i]:
            list_wait.append(i + 1)
    return json.dumps(list_wait)


# fcb92c 黄
# ff3d60 红
# 4aa3ff 浅蓝
# 343a40 黑灰
# f06292 浅红
# 8d6e63 棕
# 等待时间占比
def draw_pie_wait():
    car = ["叉车1", "叉车2", "叉车3", "叉车4", "叉车5", "叉车6", "叉车7", "叉车8"]
    num = [19.7, 26.8, 19.5, 2.7, 95.0, 92.6, 109.4, 35.1]
    pie = Pie(init_opts=opts.InitOpts(width="100%", height="360px"))
    pie.add("", [list(z) for z in zip(car, num)], radius=["40%", "75%"], center=["62%", "62%"])
    pie.set_colors(["#5664d2", "#1cbb8c", "#fcb92c", "#ff3d60", "#4aa3ff", "#343a40", "#f06292", "#8d6e63"])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="等待时间占比", title_textstyle_opts=(opts.TextStyleOpts(color='gray'))),
                        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%", legend_icon="pin",
                                                    textstyle_opts=opts.TextStyleOpts(color='gray')))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{d}%', position='inside'))
    # pie.render("templates/pages/utility/mycharts_7.html")
    return pie


def draw_pie_wait_2():
    # global no
    if no < 10845:
        data_1 = list(arr_wait[no, :])
        data_2 = list(arr_wait[no, :])
        # no += 1
    else:
        data_1 = [272.6, 278.8, 294.7, 309.2, 360.9, 360.4, 361.1, 361.5]
        data_2 = [139.6, 159.4, 226.4, 131.4, 244.4, 253.1, 259.7, 189.7]

    car = ["1", "2", "3", "4", "5", "6", "7", "8"]
    num = [19.7, 26.8, 19.5, 2.7, 95.0, 92.6, 109.4, 35.1]
    pie = Pie(init_opts=opts.InitOpts(width="100%", height="360px"))
    pie.add("", [list(z) for z in zip(car, data_1)], radius=["40%", "75%"], center=["62%", "55%"])
    pie.set_colors(["#5664d2", "#1cbb8c", "#fcb92c", "#ff3d60", "#4aa3ff", "#343a40", "#f06292", "#8d6e63"])
    pie.set_global_opts(title_opts=opts.TitleOpts(is_show=False),
                        legend_opts=opts.LegendOpts(orient="vertical", pos_top="0%", pos_left="2%", legend_icon="pin",
                                                    textstyle_opts=opts.TextStyleOpts(color='gray')))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{d}%', position='inside'))

    grid = Grid(init_opts=opts.InitOpts(width="100%", height="360px"))
    # 设置距离 bar为x轴标签过长的柱状图
    grid.add(pie, grid_opts=opts.GridOpts(pos_top="3%", pos_bottom="10%"))
    # grid.render("templates/pages/utility/mycharts_9.html")
    c = grid.dump_options_with_quotes()
    return c


# 任务完成时间
def draw_bar_time():
    # 设置主题的样式
    bar = Bar(init_opts=opts.InitOpts(width="100%", height="400px"))
    bar.add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8"])
    bar.add_yaxis("企业现行方案", [272.6, 278.8, 294.7, 309.2, 360.9, 360.4, 361.1, 361.5], category_gap="35%", color="#5664d2")
    bar.add_yaxis("新方案", [139.6, 159.4, 226.4, 131.4, 244.4, 253.1, 259.7, 189.7], category_gap="35%", color="#1cbb8c")
    # 增加主题和副标题
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="结果对比", subtitle="任务完成时间", title_textstyle_opts=(opts.TextStyleOpts(color='gray'))),
        xaxis_opts=opts.AxisOpts(name="叉车编号", name_location='center', name_gap=25, splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(name="时间/min", name_location='center', name_gap=30, splitline_opts=opts.SplitLineOpts(is_show=False)),
        legend_opts=opts.LegendOpts(pos_top="bottom", legend_icon="roundRect",
                                    textstyle_opts=opts.TextStyleOpts(color='gray'))
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[
        #         opts.MarkPointItem(type_="max", name="最大值")], symbol_size=50),
        itemstyle_opts={"normal" : {"barBorderRadius" : [5, 5, 0, 0]}},
    )
    # bar.render("templates/pages/utility/mycharts.html")
    return bar


# 方案结果对比
def draw_bar_compare():
    # 设置主题的样式
    bar = Bar(init_opts=opts.InitOpts(width="100%", height="300px"))  #
    bar.add_xaxis(["任务完成时间/min", "最大等待时间/min", "平均等待时间/min", "死锁发生次数", "碰撞发生次数"])
    bar.add_yaxis("企业现行方案", [361.5, 206.8, 188.6, 0, 15], category_gap="35%", color="#5664d2")
    bar.add_yaxis("新方案", [260.0, 109.5, 50.1, 0, 7], category_gap="35%", color="#1cbb8c")
    bar.reversal_axis()
    # 增加主题和副标题
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="方案结果对比", title_textstyle_opts=(opts.TextStyleOpts(color='gray'))),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
        legend_opts=opts.LegendOpts(pos_left="right", legend_icon="roundRect",
                                    textstyle_opts=opts.TextStyleOpts(color='gray'))
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False, position="right"),
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[
        #         opts.MarkPointItem(type_="max", name="最大值")], symbol_size=50),
        itemstyle_opts={"normal" : {"barBorderRadius" : [0, 5, 5, 0]}},
    )
    grid = Grid(init_opts=opts.InitOpts(width="100%", height="400px"))
    # 设置距离 bar为x轴标签过长的柱状图
    grid.add(bar, grid_opts=opts.GridOpts(pos_left="15%"))
    # grid.render("templates/pages/utility/mycharts_2.html")
    # bar.render("templates/pages/utility/mycharts_2.html")
    return grid


# 叉车等待时间
def draw_bar_wait():
    # 设置主题的样式
    bar = Bar(init_opts=opts.InitOpts(width="100%", height="400px"))
    bar.add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8"])
    bar.add_yaxis("企业现行方案", [184.1, 188.8, 164.0, 170.7, 199.7, 202.6, 192.0, 206.8], category_gap="35%", color="#5664d2")
    bar.add_yaxis("新方案", [19.7, 26.8, 19.5, 2.7, 95.0, 92.6, 109.4, 35.1], category_gap="35%", color="#1cbb8c")
    # 增加主题和副标题
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="结果对比", subtitle="叉车等待时间", title_textstyle_opts=(opts.TextStyleOpts(color='gray'))),
        xaxis_opts=opts.AxisOpts(name="叉车编号", name_location='center', name_gap=25, splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(name="时间/min", name_location='center', name_gap=30, splitline_opts=opts.SplitLineOpts(is_show=False)),
        legend_opts=opts.LegendOpts(pos_top="bottom", legend_icon="roundRect",
                                    textstyle_opts=opts.TextStyleOpts(color='gray'))
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[
        #         opts.MarkPointItem(type_="max", name="最大值")], symbol_size=50),
        itemstyle_opts={"normal": {"barBorderRadius": [5, 5, 0, 0]}},
    )
    # bar.render("templates/pages/utility/mycharts_3.html")
    return bar


# 灵敏度分析
def draw_bar_analysis_time():
    # 设置主题的样式
    bar = Bar(init_opts=opts.InitOpts(width="100%", height="400px"))
    bar.add_xaxis(["现行方案\n任务数80", "新方案\n任务数80", "现行方案\n任务数120", "新方案\n任务数120", "现行方案\n任务数160",
                   "新方案\n任务数160", "现行方案\n任务数200", "新方案\n任务数200"])
    bar.add_yaxis("1", [88.7, 58.2, 147.5, 95.1, 208.4, 133.9, 272.6, 139.6], category_gap="35%", color="#5664d2")
    bar.add_yaxis("2", [94.7, 72.3, 157.0, 98.0, 215.8, 140.2, 278.8, 159.4], category_gap="35%", color="#1cbb8c")
    bar.add_yaxis("3", [109.0, 81.6, 172.6, 129.0, 229.0, 155.1, 294.7, 226.4], category_gap="35%", color="#fcb92c")
    bar.add_yaxis("4", [129.0, 66.6, 181.9, 87.0, 238.6, 119.3, 309.2, 131.4], category_gap="35%", color="#ff3d60")
    bar.add_yaxis("5", [129.8, 110.0, 208.6, 161.0, 277.0, 219.8, 360.9, 244.4], category_gap="35%", color="#4aa3ff")
    bar.add_yaxis("6", [129.4, 116.1, 208.8, 156.5, 276.6, 215.0, 360.4, 253.1], category_gap="35%", color="#343a40")
    bar.add_yaxis("7", [129.7, 116.5, 208.8, 156.5, 276.7, 216.9, 361.1, 259.7], category_gap="35%", color="#f06292")
    bar.add_yaxis("8", [129.4, 80.9, 208.4, 111.0, 277.2, 158.6, 361.5, 189.7], category_gap="35%", color="#8d6e63")
    # 增加主题和副标题
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="敏感性分析", subtitle="任务完成时间", title_textstyle_opts=(opts.TextStyleOpts(color='gray'))),
        xaxis_opts=opts.AxisOpts(name_gap=10, splitline_opts=opts.SplitLineOpts(is_show=False), axislabel_opts=opts.LabelOpts(font_size=12, rotate=0)),
        yaxis_opts=opts.AxisOpts(name="时间/min", name_location='center', name_gap=30, splitline_opts=opts.SplitLineOpts(is_show=False)),
        legend_opts=opts.LegendOpts(pos_top="bottom", legend_icon="circle",
                                    textstyle_opts=opts.TextStyleOpts(color='gray'))
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[
        #         opts.MarkPointItem(type_="max", name="最大值")], symbol_size=50),
        itemstyle_opts={"normal" : {"barBorderRadius" : [5, 5, 0, 0]}},
    )
    # bar.render("templates/pages/utility/mycharts_4.html")
    return bar


def draw_bar_analysis_wait():
    # 设置主题的样式
    bar = Bar(init_opts=opts.InitOpts(width="100%", height="400px"))
    bar.add_xaxis(
        ["现行方案\n任务数80", "新方案\n任务数80", "现行方案\n任务数120", "新方案\n任务数120", "现行方案\n任务数160",
         "新方案\n任务数160", "现行方案\n任务数200", "新方案\n任务数200"])
    bar.add_yaxis("1", [49.6, 12.0, 91.6, 16.4, 136.7, 33.3, 184.1, 19.7], category_gap="35%", color="#5664d2")
    bar.add_yaxis("2", [55.7, 15.0, 98.9, 20.1, 142.5, 34.8, 188.8, 26.8], category_gap="35%", color="#1cbb8c")
    bar.add_yaxis("3", [49.0, 11.2, 95.5, 11.6, 127.2, 25.9, 164.0, 19.5], category_gap="35%", color="#fcb92c")
    bar.add_yaxis("4", [39.2, 6.2, 81.7, 3.7, 123.5, 6.0, 170.7, 2.7], category_gap="35%", color="#ff3d60")
    bar.add_yaxis("5", [66.5, 45.9, 108.8, 65.0, 151.1, 93.5, 199.7, 95.0], category_gap="35%", color="#4aa3ff")
    bar.add_yaxis("6", [57.4, 51.4, 104.3, 61.5, 137.8, 91.7, 202.6, 92.6], category_gap="35%", color="#343a40")
    bar.add_yaxis("7", [68.2, 53.8, 116.6, 63.9, 154.0, 92.6, 192.0, 109.4], category_gap="35%", color="#f06292")
    bar.add_yaxis("8", [65.8, 17.5, 113.0, 15.8, 153.7, 34.8, 206.8, 35.1], category_gap="35%", color="#8d6e63")
    # 增加主题和副标题
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="敏感性分析", subtitle="叉车等待时间", title_textstyle_opts=(opts.TextStyleOpts(color='gray'))),
        xaxis_opts=opts.AxisOpts(name_gap=10, splitline_opts=opts.SplitLineOpts(is_show=False), axislabel_opts=opts.LabelOpts(font_size=12, rotate=0)),
        yaxis_opts=opts.AxisOpts(name="时间/min", name_location='center', name_gap=30, splitline_opts=opts.SplitLineOpts(is_show=False)),
        legend_opts=opts.LegendOpts(pos_top="bottom", legend_icon="circle",
                                    textstyle_opts=opts.TextStyleOpts(color='gray'))
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[
        #         opts.MarkPointItem(type_="max", name="最大值")], symbol_size=50),
        itemstyle_opts={"normal" : {"barBorderRadius" : [5, 5, 0, 0]}},
    )
    # bar.render("templates/pages/utility/mycharts_5.html")
    return bar


# num = 0
# 实时等待时间
def draw_bar_wait_simultaneous():
    # global num
    global no
    if no < 10845:
        data_1 = list(np.around(arr_wait[no, :] / 60, 2))
        data_2 = list(np.around(arr_wait[no, :] / 60, 2))
        no += 1
    else:
        data_1 = [272.6, 278.8, 294.7, 309.2, 360.9, 360.4, 361.1, 361.5]
        data_2 = [139.6, 159.4, 226.4, 131.4, 244.4, 253.1, 259.7, 189.7]

    print(data_1)
    # 设置主题的样式
    bar = Bar(init_opts=opts.InitOpts(width="100%", height="280px"))
    bar.add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8"])
    bar.add_yaxis("新方案", data_1, category_gap="75%", color="#5664d2")  # [19.7, 26.8, 19.5, 2.7, 95.0, 92.6, 109.4, 35.1]

    line = Line(init_opts=opts.InitOpts(width="100%", height="300px"))
    line.add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8"])
    line.add_yaxis("新方案", data_2, is_smooth=True, symbol="emptyCircle", symbol_size=0, linestyle_opts=opts.LineStyleOpts(color='#1cbb8c', width=2))
    line.set_global_opts(
        title_opts=opts.TitleOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='#ffffff', width=2)),
                                 splitline_opts=opts.SplitLineOpts(is_show=False),
                                 axistick_opts=opts.AxisTickOpts(is_align_with_label=True)),
        yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show= False, linestyle_opts=opts.LineStyleOpts(color='#ffffff', width=2)),
                                 splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)),
                                 is_show= False),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    # 增加主题和副标题
    bar.set_global_opts(
        title_opts=opts.TitleOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='#ffffff', width=2)),
                                 name="叉车编号", name_location='center', name_gap=20, name_textstyle_opts=opts.TextStyleOpts(color='#858D9B'),
                                 axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                 splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=False, linestyle_opts=opts.LineStyleOpts(color='#ffffff', width=2)),
                                 name="时间/min", name_location='center', name_gap=35, name_textstyle_opts=opts.TextStyleOpts(color='#858D9B'),
                                 axistick_opts=opts.AxisTickOpts(linestyle_opts=opts.LineStyleOpts(color='#2F3549', width=1,opacity=1)),
                                 axislabel_opts=opts.LabelOpts(color='#858D9B'),
                                 splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(color='#2F3549', width=1,opacity=1)),
                                 ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    bar.set_series_opts(
        axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='#ffffff', width=2)),

        label_opts=opts.LabelOpts(is_show=False),
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[
        #         opts.MarkPointItem(type_="max", name="最大值")], symbol_size=50),
        itemstyle_opts={"normal": {"barBorderRadius": [5, 5, 0, 0]}},
    )
    grid = Grid(init_opts=opts.InitOpts(width="100%", height="300px"))
    # 设置距离 bar为x轴标签过长的柱状图
    grid.add(bar, grid_opts=opts.GridOpts(pos_top="3%", pos_bottom="10%"),)
    grid.add(line, grid_opts=opts.GridOpts(pos_top="3%", pos_bottom="10%"))
    # grid.render("templates/pages/utility/mycharts_8.html")
    c = grid.dump_options_with_quotes()
    return c


def draw_map():
    df_map = pd.read_csv('D:/ieee/Admin/map.csv')
    value = np.zeros((40, 158), dtype=int)
    for i in range(df_map.shape[0]): #df_map.shape[0] 行数
        value[df_map.iloc[i, 2] - 1][df_map.iloc[i, 1] - 1] = df_map.iloc[i, 3] #value[y][x] = (type的值) y,x从0开始

    data_map = []
    for h in range(0, 158): #0,1,...,157 x
        for w in range(0, 40): #y
            data_map.append([h, w, int(value[w][h])]) #data_map=[[x,y,type],[x,y,type],...]

    map_x_axis = [] #创建x轴标签
    for i in range(1, 159):
        map_x_axis.append(str(i))
    map_y_axis = []
    for i in range(1, 41):
        map_y_axis.append(str(i))
    for loc in arr_loc_int[no]:
        if df_map.iloc[(loc-1), 3] == 2:  #type = 2
            tmp = df_map.iloc[(loc-1), 1] * 40 + df_map.iloc[(loc-1), 2] - 41  #
            data_map[tmp][2] = 5
        else:
            tmp_1 = df_map.iloc[(loc-1), 1] * 40 + df_map.iloc[(loc-1), 2] - 41
            tmp_2 = (df_map.iloc[(loc + 828), 1]) * 40 + df_map.iloc[(loc-1), 2] - 41
            data_map[tmp_1][2] = 5
            data_map[tmp_2][2] = 5
    map = HeatMap()
    map.add_xaxis(map_x_axis)
    map.add_yaxis("坐标", map_y_axis, data_map)
    map.set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                        visualmap_opts=opts.VisualMapOpts(min_=0, max_=5, is_calculable=True,
                                                          orient="horizontal",
                                                          pos_left="center",
                                                          is_show=False,
                                                          range_color=['#1D222E', '#343a40', '#58609E',
                                                                        '#1cbb8c', '#fcb92c', '#ff3d60']), #黑 灰 蓝 绿 黄 红
                        xaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(is_show=False)),
                                                 splitline_opts=opts.SplitLineOpts(is_show=False),
                                                 is_show=False),
                        yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(is_show=False)),
                                                 splitline_opts=opts.SplitLineOpts(is_show=False),
                                                 is_show=False),
                        )

    map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    c = map.dump_options_with_quotes()
    return c



draw_bar_time()
draw_bar_compare()
draw_bar_wait()
draw_bar_analysis_time()
draw_bar_analysis_wait()
draw_pie_wait()
draw_pie_wait_2()
draw_bar_wait_simultaneous()
draw_map()