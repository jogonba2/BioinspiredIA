#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  langtons_ant.py
#  
#  Copyright 2015 Overxflow13

UP,DOWN,RIGHT,LEFT,WHITE,BLACK = 0,1,2,3,0,1

class Ant:
	
	def __init__(self,row,col):
		self.row,self.col,self.ori = row,col,DOWN
	
	def getRow(self): return self.row
	def getCol(self): return self.col
	def getPos(self): return (self.row,self.col)
	def getOri(self): return self.ori
	
	def setRow(self,row):	  self.row = row
	def setCol(self,col):	  self.col = col
	def setPos(self,row,col): self.row,self.col = row,col
	def setOri(self,ori):	  self.ori = ori
	
	def makeStep(self,color,rows,cols):
		self.turnRight() if color==WHITE else self.turnLeft()
		self.nextCell(rows,cols)
		return BLACK if color==WHITE else WHITE
		
	def turnRight(self):
		if   self.ori==UP:    self.ori = RIGHT
		elif self.ori==RIGHT: self.ori = DOWN
		elif self.ori==DOWN:  self.ori = LEFT
		elif self.ori==LEFT:  self.ori = UP

	def turnLeft(self):
		if   self.ori==UP:    self.ori = LEFT
		elif self.ori==RIGHT: self.ori = UP
		elif self.ori==DOWN:  self.ori = RIGHT
		elif self.ori==LEFT:  self.ori = DOWN
	
	def nextCell(self,rows,cols):
		""" Toroidal 2d space """
		if self.ori==UP:    self.row = (self.row-1)%rows
		if self.ori==RIGHT: self.col = (self.col+1)%rows
		if self.ori==DOWN:  self.row = (self.row+1)%rows
		if self.ori==LEFT:  self.col = (self.col-1)%rows
	
class Table:
	
	def __init__(self,rows,cols,color):
		self.table,self.rows,self.cols,self.color = None,rows,cols,color
		self.initTable()
	
	def getRows(self):          return self.rows
	def getCols(self): 		    return self.cols
	def getColor(self,row,col): return self.table[row][col]
	
	def setRows(self,rows):		       self.rows = rows
	def setCols(self,cols): 	       self.cols = cols
	def setColor(self,row,col,color):  self.table[row][col] = color
	
	def initTable(self): 
		self.table = [[] for row in xrange(self.rows)]
		for i in xrange(self.rows):
			for j in xrange(self.cols):
				self.table[i].append(self.color)
		
	def __str__(self,antRow,antCol): 
		for i in xrange(24): print
		for row in xrange(self.getRows()): 
			for col in xrange(self.getCols()):
				if row==antRow and col==antCol: print "*",
				else: print self.getColor(row,col),			 
			print "\n"

class AntAC:
	
	def __init__(self,row,col,rows,cols,color,steps):
		self.ant,self.table,self.steps = Ant(row,col),Table(rows,cols,color),steps
	
	def __run__(self):
		steps = 0
		while steps<=self.steps:			
			antRow,antCol = self.ant.getRow(),self.ant.getCol()
			newColor = self.ant.makeStep(self.table.getColor(antRow,antCol),self.table.getRows(),self.table.getCols())
			self.table.setColor(antRow,antCol,newColor)			
			antRow,antCol = self.ant.getRow(),self.ant.getCol()
			self.table.__str__(antRow,antCol)
			self.__str__()
			steps += 1; raw_input()
			
	def __str__(self):
		print "\t----- INFO -----\n"
		print "-> Ant row:",self.ant.getRow()
		print "-> Ant col:",self.ant.getCol()
		print "-> Cell color:",self.table.getColor(self.ant.getRow(),self.ant.getCol())
		print "-> Ant orientation:",self.ant.getOri()

			 
a = AntAC(5,5,10,10,BLACK,100)
a.__run__()
