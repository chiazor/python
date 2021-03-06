# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2015-2017 BigML
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


""" Testing local prediction

"""
from world import world, setup_module, teardown_module
import compare_predictions_steps as prediction_compare


class TestLocalPrediction(object):

    def setup(self):
        """
            Debug information
        """
        print "\n-------------------\nTests in: %s\n" % __name__

    def teardown(self):
        """
            Debug information
        """
        print "\nEnd of tests in: %s\n-------------------\n" % __name__

    def test_scenario1(self):
        """
            Scenario: Successfully creating a prediction from a local model in a json file:
                Given I create a local model from a "<model>" file
                When I create a local prediction for "<data_input>" with confidence
                Then the local prediction is "<prediction>"
                And the local prediction's confidence is "<confidence>"

                Examples:
                | model                | data_input    |  prediction  | confidence
                | ../data/iris_model.json | {"petal length": 0.5} | Iris-setosa | 0.90594

        """
        print self.test_scenario1.__doc__
        examples = [
            ['data/iris_model.json', '{"petal length": 0.5}', 'Iris-setosa', '0.90594']]
        for example in examples:
            print "\nTesting with:\n", example
            prediction_compare.i_create_a_local_model_from_file(self, example[0])
            prediction_compare.i_create_a_local_prediction_with_confidence(self, example[1])
            prediction_compare.the_local_prediction_is(self, example[2])
            prediction_compare.the_local_prediction_confidence_is(self, example[3])


    def test_scenario2(self):
        """
            Scenario: Successfully creating a multiple prediction from a local model in a json file:
                Given I create a local model from a "<model>" file
                When I create a multiple local prediction for "<data_input>"
                Then the multiple local prediction is "<prediction>"

                Examples:
                | model                | data_input    | prediction
                | ../data/iris_model.json | {"petal length": 3} |  [{"count": 42, "confidence": 0.4006020980792863, "prediction": "Iris-versicolor", "probability": 0.5060240963855421}, {"count": 41, "confidence": 0.3890868795664999, "prediction": "Iris-virginica", "probability": 0.4939759036144578}]
        """
        print self.test_scenario1.__doc__
        examples = [
            ['data/iris_model.json', '{"petal length": 3}',  '[{"count": 42, "confidence": 0.4006020980792863, "prediction": "Iris-versicolor", "probability": 0.5060240963855421}, {"count": 41, "confidence": 0.3890868795664999, "prediction": "Iris-virginica", "probability": 0.4939759036144578}]']]
        for example in examples:
            print "\nTesting with:\n", example
            prediction_compare.i_create_a_local_model_from_file(self, example[0])
            prediction_compare.i_create_a_multiple_local_prediction(self, example[1])
            prediction_compare.the_multiple_local_prediction_is(self, example[2])
