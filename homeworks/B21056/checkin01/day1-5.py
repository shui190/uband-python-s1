#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
def main():
	who = ' 饼央 '
	good_price = 2
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2
	aaa = reasonable_price - good_price

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		if aaa > 2:
			print '她买了 4 斤' 
		else:
			print '她买了 %d 斤' % (buy_amount + aaa)
 	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'

if __name__ == '__main__':
  main()