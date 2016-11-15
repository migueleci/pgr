from SCCPVisitor import SCCPVisitor

class RewriterVisitor(SCCPVisitor):
	def visitLine(self, ctx):
		data = self.visit(ctx.proc())
		print('[process, root, {0}]'.format(data))
		return '{0}'.format(data)

	def visitProcloc(self, ctx):
		data = self.visit(ctx.proc())
		INT = ctx.INT()
		# print('prlc at {0}: {1}'.format(INT, data))
		return '< {0} >[{1}]'.format(INT, data)

	def visitParallel(self, ctx):
		left = self.visit(ctx.proc(0))
		right = self.visit(ctx.proc(1))
		# print('parallel: {0} || {1}'.format(left,right))
		return '(({0}) || ({1}))'.format(left,right)

	def visitAsk(self, ctx):
		cmd = self.visit(ctx.proc())
		const = self.visit(ctx.const())
		if ctx.loc() != None:
			loc = self.visit(ctx.loc())
			# print('ask at {0} if {1}: {2}'.format(loc, const, cmd))
			return '(ask< {0} >({1}) -> {2})'.format(loc, const, cmd)
		else:
			# print('ask if {0}: {1}'.format(const, cmd))
			return '(ask({0}) -> {1})'.format(const, cmd)

	def visitTell(self, ctx):
		data = self.visit(ctx.const())
		# print('tell: {0}'.format(data))
		return 'tell ({0})'.format(data)

	def visitExpr(self, ctx):
		op = ctx.op().getText()
		if ctx.INT() != None:
			ID  = ctx.ID(0)
			INT = ctx.INT()
			return '{0}:Integer {1} {2}'.format(ID, op, INT)
		else: 
			left = ctx.ID(0)
			right = ctx.ID(1)
			return '{0}:Integer {1} {2}:Integer'.format(left, op, right)
		
	def visitLoc(self, ctx):
		l = len(ctx.INT())
		loc = ''
		for i in range(l):
			loc += str(ctx.INT(i)) if i==0 else ' . '+str(ctx.INT(i))
		return loc

	def visitInt(self, ctx):
		return ctx.INT().getText()

	def visitId(self, ctx):
		return ctx.ID().getText()+":Boolean"

	def visitBool(self, ctx):
		return ctx.BOOL().getText()

	