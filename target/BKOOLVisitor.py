# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_name.
    def visitClass_name(self, ctx:BKOOLParser.Class_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_member.
    def visitClass_member(self, ctx:BKOOLParser.Class_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_decl.
    def visitAttribute_decl(self, ctx:BKOOLParser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_kw.
    def visitAttribute_kw(self, ctx:BKOOLParser.Attribute_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_list.
    def visitAttribute_list(self, ctx:BKOOLParser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decl.
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#para_list.
    def visitPara_list(self, ctx:BKOOLParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#cstor_name.
    def visitCstor_name(self, ctx:BKOOLParser.Cstor_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#main_method.
    def visitMain_method(self, ctx:BKOOLParser.Main_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_decl.
    def visitArr_decl(self, ctx:BKOOLParser.Arr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_list.
    def visitArr_list(self, ctx:BKOOLParser.Arr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_decl.
    def visitObj_decl(self, ctx:BKOOLParser.Obj_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_list.
    def visitObj_list(self, ctx:BKOOLParser.Obj_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_name.
    def visitObj_name(self, ctx:BKOOLParser.Obj_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#int_typ.
    def visitInt_typ(self, ctx:BKOOLParser.Int_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#float_typ.
    def visitFloat_typ(self, ctx:BKOOLParser.Float_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_typ.
    def visitBool_typ(self, ctx:BKOOLParser.Bool_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#string_typ.
    def visitString_typ(self, ctx:BKOOLParser.String_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#void_typ.
    def visitVoid_typ(self, ctx:BKOOLParser.Void_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_typ.
    def visitArr_typ(self, ctx:BKOOLParser.Arr_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_typ.
    def visitClass_typ(self, ctx:BKOOLParser.Class_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atom.
    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_block.
    def visitStmt_block(self, ctx:BKOOLParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_block_wo_return.
    def visitStmt_block_wo_return(self, ctx:BKOOLParser.Stmt_block_wo_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asm_stmt.
    def visitAsm_stmt(self, ctx:BKOOLParser.Asm_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt.
    def visitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalar_var.
    def visitScalar_var(self, ctx:BKOOLParser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invo.
    def visitMethod_invo(self, ctx:BKOOLParser.Method_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invoke_stmt.
    def visitInvoke_stmt(self, ctx:BKOOLParser.Invoke_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#argu_list.
    def visitArgu_list(self, ctx:BKOOLParser.Argu_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_lit.
    def visitBool_lit(self, ctx:BKOOLParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_lit.
    def visitArr_lit(self, ctx:BKOOLParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_value.
    def visitArr_value(self, ctx:BKOOLParser.Arr_valueContext):
        return self.visitChildren(ctx)



del BKOOLParser