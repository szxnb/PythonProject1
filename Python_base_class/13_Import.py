
# # 通过akshare获取今天最新的股市数据
# import akshare as ak
# # 获取今天的股票数据
# stock_zh_a_today_df = ak.stock_zh_a_daily(symbol="sh603843", adjust="qfq")

# #存入字典
# stock_dict = {
#     "date": stock_zh_a_today_df["date"],
#     "open": stock_zh_a_today_df["open"],
#     "high": stock_zh_a_today_df["high"],
#     "low": stock_zh_a_today_df["low"],
#     "close": stock_zh_a_today_df["close"],
#     "volume": stock_zh_a_today_df["volume"],
#     "amount": stock_zh_a_today_df["amount"]
# }

# print(stock_dict)

