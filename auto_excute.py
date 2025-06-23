import subprocess

def run_c_program(program_path, input_file=None):
    command = [program_path]+input_file
    print(command)

    try:
        #print("ssd:"+program_path+" trace: "+input_file[1])
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,bufsize=1, universal_newlines=True)
        while True:
             process.stdin.flush()
             output = process.stdout.readline()
             if output == '' and process.poll() is not None:
                break
             print(output,end="",flush=True)
        if result.returncode == 0:
            print("程序成功执行")
        else:
            print(f"程序执行失败，返回码: {result.returncode}")
            print("trace: "+ input_file[2])
            print("错误输出:\n", result.stderr)
    except Exception as e:
        print(f"发生错误: {e}")
        print("trace: "+ input_file[2])

if __name__ == "__main__":
    c_program_path = "./ssd"  # 替换为你的C语言程序的路径
    # arg = [ #trace_times, trace_name, block.csv
    #      ["30","../new_trace/web2_pre.csv","1"],
    #       ["30","../new_trace/ads_flag.csv","1"],
    #        ["30","../new_trace/hm_1.csv","1"],
    #        ["30","../newlun/2016021719-LUN3.csv","1"],
    #        ["30","../newlun/2016021813-LUN6.csv","1"],
    #        ["30","../newlun/2016021710-LUN3.csv","1"]
    #     ]
    # arg = [
    # ["30","../new_trace/web2_pre.csv","1"],
    # ["60","../new_trace/ads_flag.csv","1"],
    # ["30","../newlun/2016021719-LUN3.csv","1"],
    # ["30","../newlun/2016021813-LUN6.csv","1"],
    # ["30","../newlun/2016021710-LUN3.csv","1"],
    # ["30","../newlun/2016021714-LUN3.csv","1"],
    # ["30","../newlun/2016021708-LUN3.csv","1"],
    # ["30","../newlun/2016021715-LUN3.csv","1"],
    # ["30","../newlun/2016021812-LUN6.csv","1"],
    # ["30","../newlun/2016021711-LUN3.csv","1"],
    # ["30","../newlun/2016021615-LUN6.csv","1"],
    # ["30","../newlun/2016021619-LUN0.csv","1"]
    # ]
    # arg = [
    # ["30","../newlun/2016021812-LUN6.csv","1","15658456"],
    # ["30","../newlun/2016021714-LUN3.csv","1","13729380"],
    # ["30","../newlun/2016021813-LUN6.csv","1","17305216"],
    #  ["30","../newlun/2016021719-LUN3.csv","1","12885302"]
    # ]
    # arg = [
    # ["30","../newlun/2016021812-LUN0.csv","1","19558364"],
    # ["30","../newlun/2016021613-LUN6.csv","1","20903514"],
    # ["30","../newlun/2016021810-LUN6.csv","1","23124808"],
    # ]
    # arg = [
    # ["30","../newlun/2016021712-LUN3.csv","1","17933144"],
    # ["30","../newlun/2016021714-LUN1.csv","1","15782490"],
    # ["30","../newlun/2016021612-LUN2.csv","1","17047312"],
    # ["30","../newlun/2016021812-LUN1.csv","1","22710774"],
    # ["30","../newlun/2016021810-LUN4.csv","1","18728738"],
    # ["30","../newlun/2016021811-LUN3.csv","1","14459642"],
    # ]
    # arg = [
    # ["15","../new_trace/proj_3.csv","1","2973626"],
    # ["15","../new_trace/proj_4.csv","1","27976454"],
    # ["15","../new_trace/src2_1.csv","1","9495064"],
    # ["15","../new_trace/usr_0.csv","1","1291004"]
    # ]
    # arg = [
    # ["30","../newlun/2016021808-LUN0.csv","1","0","1"],
    # ["30","../newlun/2016021713-LUN3.csv","1","0","1"],
    # ["30","../newlun/2016021813-LUN6.csv","1","0","1"],
    # ["30","../newlun/2016021613-LUN6.csv","1","0","1"],
    # ["30","../newlun/2016021708-LUN3.csv","1","0","1"],
    # ["30","../newlun/2016021812-LUN6.csv","1","0","1"],
    # ["30","../newlun/2016021711-LUN3.csv","1","0","1"],
    # ["30","../newlun/2016021812-LUN0.csv","1","0","1"],
    # ["30","../newlun/2016021612-LUN4.csv","1","0","1"],
    # ["30","../newlun/2016021810-LUN2.csv","1","0","1"],
    # ["15","../new_trace_order/web1_pre.csv","1","0","1"],
    # ["15","../new_trace_order/web2_pre.csv","1","0","1"],
    # ["15","../new_trace_order/ads_flag.csv","1","0","1"],
    # ["15","../new_trace_order/hm_1.csv","1","0","1"],
    # ["15","../new_trace_order/usr_0.csv","1","0","4"],
    # ["15","../new_trace_order/proj_4.csv","1","0","4"],
    # ["15","../new_trace_order/proj_3.csv","1","0","4"],
    # ["15","../new_trace_order/web_1.csv","1","0","4"],
    # ["15","../new_trace_order/web_2.csv","1","0","4"],
    # ["15","../new_trace_order/web_0.csv","1","0","4"]
    # ]
    arg = [
        # ["1","./msrc/hm_1.csv"],
        # ["1","./msrc/wdev_0.csv"],
        # ["1","./Ali/735"],
        # ["1","./Ali/206"],
        # ["1","./Ali/127_0_168"],
        # ["1","./Ali/139_0_168"],
        # ["1","./Ali/112"],
        # ["1","./Ali/121"],
        # ["1","./LUN/2016021614-LUN0.csv"],
        # ["1","./Ali/108_0_168"],
        # ["1","./Ali/188"],
        # ["1","./Ali/373"],
        # ["1","./Ali/49_0_24.csv"],
        # ["1","./Ali/Ali_72h_44"],
        # ["1","./Ali/Ali_72h_858"],

        # ["1","./Ali/42_0_24.csv"],
        # ["1","./Ali/49_0_24.csv"],
        # ["1","./Ali/82_0_168"],
        # ["1","./Ali/Ali_72h_44"],
        # ["1","./Ali/188"],
        # ["1","./Ali/373"],
        # ["1","./Ali/505_0_24.csv"],
        # ["1","./Ali/Ali_72h_858"],
        # ["1","./Ali/143_0_168"],

        # ["1","./big/mds_1.csv"],
        # ["1","./big/stg_1.csv"],
        # ["1","./big/web_2.csv"],
        # ["1","./big/2016021612-LUN1.csv"],
        # ["1","./big/2016021811-LUN4.csv"],
        # ["1","./big/2016021813-LUN0.csv"],
        # ["1","./big/2016021813-LUN4.csv"],
        ["1","./big/2016021615-LUN0.csv"],
        ["1","./big/2016021710-LUN2.csv"],
        ["1","./big/2016021712-LUN1.csv"],
        ["1","./big/2016021715-LUN0.csv"],
        ["1","./big/2016021812-LUN3.csv"],
        ["1","./big/prn_0.csv"],
        ["1","./big/src2_2.csv"],


        # ["1","./LUN/2016021807-LUN0.csv"],
        # ["1","./LUN/2016021807-LUN2.csv"],
        # ["1","./LUN/2016021807-LUN6.csv"],
        # ["1","./msrc/rsrch_2.csv"],
        # ["1","./msrc/ads_flag.csv"],
        # ["1","./LUN/2016021707-LUN2.csv"],
        # ["1","./LUN/2016021718-LUN4.csv"],
        # ["1","./Ali/143_0_168"],
        # ["1","./Ali/44_0_24.csv"],
        # ["1","./Ali/858_0_24.csv"],
        # ["1","./Ali/998_0_24.csv"]

        # ["1","./LUN/2016021807-LUN0.csv"],
        # ["1","./LUN/2016021807-LUN2.csv"],
        # ["1","./LUN/2016021807-LUN6.csv"],
        # ["1","./msrc/rsrch_2.csv"],
        # ["1","./msrc/ads_flag.csv"],
        # ["1","./LUN/2016021707-LUN2.csv"],
        # ["1","./LUN/2016021718-LUN4.csv"],
        # ["1","./Ali/143_0_168"],
        # ["1","./Ali/44_0_24.csv"],
        # ["1","./Ali/858_0_24.csv"],
        # ["1","./Ali/998_0_24.csv"]
        # ["1","./msrc/hm_1.csv"],
        # ["1","./msrc/wdev_0.csv"],
        # ["1","./msrc/web_3.csv"],
        # ["1","./Ali/110_0_168"],
        # ["1","./Ali/119_0_168"],
        # ["1","./Ali/127_0_168"],
        # ["1","./Ali/139_0_168"],
        # ["1","./Ali/14_0_24.csv"]
        # ["1","./Ali/143_0_168"],
        # ["1","./Ali/14_0_24.csv"],

        # ["1","./Ali/110_0_168"],
        # ["1","./LUN/2016021614-LUN0.csv"],
        # ["1","./LUN/2016021614-LUN4.csv"],
        # ["1","./LUN/2016021615-LUN1.csv"],
        # ["1","./LUN/2016021616-LUN6.csv"],
        # ["1","./msrc/hm_0.csv"],

    # ["1","../newlun/2016021808-LUN0.csv","1","0","4","64"],
    # ["1","../newlun/2016021808-LUN0.csv","1","0","4","128"],
    # ["1","../newlun/2016021808-LUN0.csv","1","0","4","256"],
    # ["1","../newlun/2016021808-LUN0.csv","1","0","4","512"],
    # ["1","../newlun/2016021808-LUN0.csv","1","0","4","1024"],
    # ["1","../newlun/2016021812-LUN6.csv","1","0","4","64"],
    # ["1","../newlun/2016021812-LUN6.csv","1","0","4","128"],
    # ["1","../newlun/2016021812-LUN6.csv","1","0","4","256"],
    # ["1","../newlun/2016021812-LUN6.csv","1","0","4","512"],
    # ["1","../newlun/2016021812-LUN6.csv","1","0","4","1024"],
    # ["1","../newlun/2016021711-LUN3.csv","1","0","4","64"],
    # ["1","../newlun/2016021711-LUN3.csv","1","0","4","128"],
    # ["1","../newlun/2016021711-LUN3.csv","1","0","4","256"],
    # ["1","../newlun/2016021711-LUN3.csv","1","0","4","512"],
    # ["1","../newlun/2016021711-LUN3.csv","1","0","4","1024"],
    # ["1","../newlun/2016021812-LUN6.csv","1","0","4","64"],
    # ["1","../newlun/2016021812-LUN0.csv","1","0","4","128"],
    # ["1","../newlun/2016021812-LUN0.csv","1","0","4","256"],
    # ["1","../newlun/2016021812-LUN0.csv","1","0","4","512"],
    # ["1","../newlun/2016021812-LUN0.csv","1","0","4","1024"],
    # ["1","../new_trace_order/usr_0.csv","1","0","4","64"],
    # ["1","../new_trace_order/usr_0.csv","1","0","4","128"],
    # ["1","../new_trace_order/usr_0.csv","1","0","4","256"],
    # ["1","../new_trace_order/usr_0.csv","1","0","4","512"],
    # ["1","../new_trace_order/usr_0.csv","1","0","4","1024"],
    # ["1","../new_trace_order/web_0.csv","1","0","4","64"],
    # ["1","../new_trace_order/web_0.csv","1","0","4","128"],
    # ["1","../new_trace_order/web_0.csv","1","0","4","256"],
    # ["1","../new_trace_order/web_0.csv","1","0","4","512"],
    # ["1","../new_trace_order/web_0.csv","1","0","4","1024"],
    # ["1","../ali/121","1","0","4","64"],
    # ["1","../ali/121","1","0","4","128"],
    # ["1","../ali/121","1","0","4","256"],
    # ["1","../ali/121","1","0","4","512"],
    # ["1","../ali/121","1","0","4","1024"]
    ]
    # arg = [
    #     ["1","../new_trace/ads_flag.csv","1"]
    # ]
    result = subprocess.run(["make","clean"], shell=False, text=True, capture_output=True)
    print("程序输出:\n", result.stdout)
    result = subprocess.run(["make","all"], shell=False, text=True, capture_output=True)
    print("程序输出:\n", result.stdout)
    for i in arg:
        run_c_program(c_program_path,i)
