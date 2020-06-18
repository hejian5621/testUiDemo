import xlwt







class CellStyle:
    """电子单元格样式"""




    # 样式：居中
    def spreadsheet_CreateAForm_style_alignCenter(self):
        style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
        al = xlwt.Alignment()
        al.horz = 0x02  # 设置水平居中
        al.vert = 0x01  # 设置垂直居中
        al.wrap = 1  # 换行
        return al


    # 样式：添加边框
    def spreadsheet_CreateAForm_style_rim(self):
        borders = xlwt.Borders()  # 创建边界
        borders.left = xlwt.Borders.THIN  # DASHED:虚线  NO_LINE:没有 THIN:实线
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40
        return borders



