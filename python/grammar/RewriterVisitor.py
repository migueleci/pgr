from SCCPVisitor import SCCPVisitor

class RewriterVisitor(SCCPVisitor):
	def visitSys(self, ctx):
		spec = self.visit(ctx.body())
		if ctx.decl() != None:
			data = self.visit(ctx.decl())
			for i in data[0]:
				spec = spec.replace(i+' ',i+":Integer ")
				spec = spec.replace(i+')',i+":Integer)")
			for b in data[1]:
				spec = spec.replace(b+' ',b+":Boolean ")
				spec = spec.replace(b+')',b+":Boolean)")
		print('{0}'.format(spec))
		return '{0}'.format(spec)

	def visitDecl(self, ctx):
		ids = []
		lint = []
		if ctx.vint() != None:
			for i in range(len((ctx.vint()))):
				lint.extend(self.visit(ctx.vint(i)))
		lbool = []
		if ctx.vbool() != None:
			for i in range(len((ctx.vbool()))):
				lbool.extend(self.visit(ctx.vbool(i)))
		ids.append(lint)
		ids.append(lbool)
		# print(ids)
		return ids

	def visitVint(self, ctx):
		ldata = len(ctx.ID())
		ids = []
		for i in range(ldata):
			ids.append(str(ctx.ID(i)))
		# print('int: ',ids)
		return ids

	def visitVbool(self, ctx):
		ldata = len(ctx.ID())
		ids = []
		for i in range(ldata):
			ids.append(str(ctx.ID(i)))
		# print('bool: ',ids)
		return ids

	def visitBody(self, ctx):
		ldata = len(ctx.line())
		data = 'rew { [store, root, true] '
		for i in range(ldata):
			data += ' '+self.visit(ctx.line(i))
		data += ' } .'
		# print('{0}'.format(data))
		return '{0}'.format(data)

	def visitLine(self, ctx):
		data = self.visit(ctx.proc())
		# print('[process, root, {0}]'.format(data))
		return '[process, root, {0}]'.format(data)

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
		if op == '=':
			op = '==='
		if ctx.INT() != None:
			ID  = ctx.ID(0)
			INT = ctx.INT()
			return '{0} {1} {2}'.format(ID, op, INT)
			# return '{0}:Integer {1} {2}'.format(ID, op, INT)
		else: 
			left = ctx.ID(0)
			right = ctx.ID(1)
			return '{0} {1} {2}'.format(left, op, right)
			# return '{0}:Integer {1} {2}:Integer'.format(left, op, right)
		
	def visitLoc(self, ctx):
		l = len(ctx.INT())
		loc = ''
		for i in range(l):
			loc += str(ctx.INT(i)) if i==0 else ' . '+str(ctx.INT(i))
		return loc

	def visitInt(self, ctx):
		return ctx.INT().getText()

	def visitId(self, ctx):
		return ctx.ID().getText() #+":Boolean"

	def visitBool(self, ctx):
		return ctx.BOOL().getText()

	