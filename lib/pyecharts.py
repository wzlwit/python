# visualization

from pyecharts import bar
from pyecharts import options as opts

bar = (
    Bar()
    .add_xaxis(["item1","item2",'...'])
    .add_yaxis("storeA",[12,23,33])
    .add_yaxis("storeB",[31,32,44])
    .add_global_opts(title_opts=opts.TitleOpts(title="sales"))
)
bar.render()