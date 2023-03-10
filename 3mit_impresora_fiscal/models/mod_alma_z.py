# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import api, fields, models, tools, _


class DatosZdiarios(models.Model):
    _name = "datos.zeta.diario"
    _description = "Se almacena los Z diarios apartir de las impresiones de Z desde la impresora."
    
    numero_ultimo_reporte_z = fields.Char()
    fecha_ultimo_reporte_z = fields.Char()
    hora_ultimo_reporte_z = fields.Char()
    numero_ultima_factura = fields.Char()
    fecha_ultima_factura = fields.Char()
    hora_ultima_factura = fields.Char()
    numero_ultima_nota_de_debito = fields.Char()
    numero_ultima_nota_de_credito = fields.Char()
    numero_ultimo_doc_no_fiscal = fields.Char()
    ventas_exento = fields.Char()
    base_imponible_ventas_iva_g = fields.Char()
    impuesto_iva_g = fields.Char()
    base_imponible_ventas_iva_r = fields.Char()
    impuesto_iva_r = fields.Char()
    base_imponible_ventas_iva_a = fields.Char()
    impuesto_iva_a = fields.Char()
    nota_de_debito_exento = fields.Char()
    bi_iva_g_en_nota_de_debito = fields.Char()
    impuesto_iva_g_en_nota_de_debito = fields.Char()
    bi_iva_r_en_nota_de_debito = fields.Char()
    impuesto_iva_r_en_nota_de_debito = fields.Char()
    bi_iva_a_en_nota_de_debito = fields.Char()
    impuesto_iva_a_en_nota_de_debito = fields.Char()
    nota_de_credito_exento = fields.Char()
    bi_iva_g_en_nota_de_credito = fields.Char()
    impuesto_iva_g_en_nota_de_credito = fields.Char()
    bi_iva_r_en_nota_de_credito = fields.Char()
    impuesto_iva_r_en_nota_de_credito = fields.Char()
    bi_iva_a_en_nota_de_credito = fields.Char()
    impuesto_iva_a_en_nota_de_credito = fields.Char()
    company_id = fields.Integer()