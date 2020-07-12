#!/usr/bin/emv python
# -*- coding: utf-8 -*-
import decimal

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a ,b):
        return float((decimal.Decimal(a) * decimal.Decimal(b)).quantize(decimal.Decimal('0.00')))

    def div(self, a, b):
        return float((decimal.Decimal(a) / decimal.Decimal(b)).quantize(decimal.Decimal('0.00')))



