import pandas as pd


def read_file(fname):
    """Takes a text file from the National Cancer Institute's
    SEER datbase for the data files in the incidence/yr1973_2015.seer9,
    yr1992_2015.sj_la_rg_ak, yr2000_2015.ca_ky_lo_nj_ga , and yr2005.lo_2nd_half directories.
    Returns a Pandas DataFrame. Dataset at: https://seer.cancer.gov/"""
    with open(fname) as f:
        content = f.readlines()
    

    factor_names = ('PUBCSNUM', 'REG', 'MAR_STAT', 'RACE1V', 'NHIADE', 'SEX', 'AGE_DX', 'YR_BRTH', 
          'SEQ_NUM', 'MDXRECMP', 'YEAR_DX', 'PRIMSITE', 'LATERAL', 'HISTO2V', 'BEHO2V', 'HISTO3V', 
          'BEHO3V', 'GRADE', 'DX_CONF', 'REPT_SRC', 'EOD10_SZ', 'EOD10_EX', 'EOD10_PE', 'EOD10_ND', 
          'EOD10_PN', 'EOD10_NE', 'EOD13', 'EOD2', 'EOD4', 'EOD_CODE', 'TUMOR_1V', 'TUMOR_2V', 
          'TUMOR_3V', 'CSTUMSIZ', 'CSEXTEN', 'CSLYMPHN', 'CSMETSDX', 'CS1SITE', 'CS2SITE', 'CS3SITE', 
          'CS4SITE', 'CS5SITE', 'CS6SITE', 'CS25SITE', 'DAJCCT', 'DAJCCN', 'DAJCCM', 'DAJCCSTG',
          'DSS1977S', 'DSS2000S', 'DAJCCFL', 'CSVFIRST', 'CSVLATES', 'CSVCURRENT', 'SURGPRIF', 'SURGSCOF', 
          'SURGSITF', 'NUMNODES', 'NO_SURG', 'SS_SURG', 'SURGSCOP', 'SURGSITE', 'REC_NO', 'TYPE_FU',
          'AGE_1REC', 'SITERWHO', 'ICDOTO9V', 'ICDOT10V', 'ICCC3WHO', 'ICCC3XWHO', 'BEHTREND', 'HISTREC',
          'HISTRECB', 'cs0204schema', 'RAC_RECA', 'RAC_RECY', 'ORIGRECB', 'HST_STGA', 'AJCC_STG', 
          'AJ_3SEER', 'SSS77VZ', 'SSSM2KPZ', 'FIRSTPRM', 'ST_CNTY', 'CODPUB', 'CODPUBKM', 'STAT_REC',
          'IHSLINK', 'SUMM2K', 'AYASITERWHO', 'LYMSUBRWHO', 'VSRTSADX', 'ODTHCLASS', 'CSTSEVAL', 'CSRGEVAL',
          'CSMTEVAL', 'intprim', 'erstatus', 'prstatus', 'csschema', 'CS8SITE', 'CS10SITE', 'CS11SITE',
          'CS13SITE', 'CS15SITE', 'CS16SITE', 'VASINV', 'srv_time_mon', 'srv_time_mon_flag', 'INSREC_PUB',
          'DAJCC7T', 'DAJCC7N', 'DAJCC7M', 'DAJCC7STG', 'ADJTM_6VALUE', 'ADJNM_6VALUE', 'ADJM_6VALUE',
          'ADJAJCCSTG', 'CS7SITE', 'CS9SITE', 'CS12SITE', 'her2', 'brst_sub', 'ANNARBOR', 'CSMETSDXB_PUB',
          'CSMETSDXBR_PUB', 'CSMETSDXLIV_PUB', 'CSMETSDXLUNG_PUB', 'T_VALUE', 'N_VALUE', 'M_VALUE', 
          'MALIGCOUNT', 'BENBORDCOUNT')
          
    factor_sizes = ((0,8), (8,18), (18,19), (19,21), (22,23), (23,24), (24,27), (27,31), (34,36),(36,38),
              (38,42), (42,46), (46,47), (47,51), (51,52), (52,56), (56,57), (57,58), (58,59), (59,60),
              (60,63), (63,65), (65,67), (67,68), (68,70), (70,72), (72,85), (85,87), (87,91), (91,92), 
              (92,93), (93,94), (94,95), (95,98), (98,101), (101,104), (104,106), (106,109), (109,112), 
              (112,115), (115,118), (118,121), (121,124), (124,127), (127,129), (129,131), (131,133), 
              (133,135), (135,136), (136,137), (137,138), (140,146), (146,152), (152,158), (158,160), 
              (160,161), (161,162), (162,164), (164,165), (169,171), (173,174), (174,175), (175,177), 
              (190,191), (191,193), (198,203), (203,207), (207,211), (217,220), (220,223), (223, 224), 
              (226,227), (227,229), (229,232), (232,233), (233,234), (234,235), (235,236), (236,238), 
              (238,240), (240,241), (241,242), (244,245), (245,250), (254,259), (259,264), (264,265), 
              (265,266), (266,267), (267,269), (269,271), (271,272), (272,273), (273,274), (274,275), 
              (275,276), (276,277), (277,278), (278,279), (279,281), (281,284), (284,287), (287,290), 
              (290,293), (293,296), (296,299), (299,300), (300,304), (304,305), (310,311), (311,314),
              (314,317), (317,320), (320,323), (323,325), (325,327), (327,329), (329,331), (331,334),
              (334,337), (337,340), (340,341), (341,342), (347,348), (348,349), (349,350), (350,351), 
              (351,352), (352,353), (354,355), (356,357), (358,360), (360,362))
    content_list = list()
 
    for row in enumerate(content):
        r, d = row
        content_list.append([])
        for size in factor_sizes:
            a, b = size
            content_list[r].append(d[a:b])
    
    df = pd.DataFrame(content_list, columns=factor_names)    

    return df
   