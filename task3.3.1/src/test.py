import pandas as pd

data = pd.read_excel(r"C:\Users\47047\Desktop\r_nccn_config.xlsx",sheet_name="r_nccn_config")

gene_list = data["ftest_gene"]
content_list = data["ftest_content"]
order_list = data["forder"]

nccn_list = []
for i in range(len(gene_list)):
    tmp_dict = {}
    tmp_dict["fid"] = i+1
    tmp_dict["ftype_code"] = "NCCN-HuaXi-59"
    tmp_dict["ftarget_drug"] = ""
    tmp_dict["fdetect_gene"] = gene_list[i]
    tmp_dict["fdetect_content"] = content_list[i]
    tmp_dict["forder"] = str(order_list[i])
    nccn_list.append(tmp_dict)
print(nccn_list)