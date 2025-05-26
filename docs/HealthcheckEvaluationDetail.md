# HealthcheckEvaluationDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**dict(str, Object)**](Object.md) | Optional details of the evaluation - raw data | [optional] 
**hash** | **str** | Unique identifier | [optional] 
**id** | **str** | Unique identifier of item | [optional] 
**name** | **str** | Name of item | [optional] 
**node** | **str** | Either &#39;cluster&#39; or an lnn | [optional] 
**parameters** | [**Empty**](Empty.md) | The parameters used in this item evaluation | [optional] 
**passed** | **bool** | True if the item returned no failures | [optional] 
**status** | **str** | Health status based on default thresholds | [optional] 
**value** | **int** | Normalized measured value 0 (bad) to 100 (perfect) or -1 for unsupported | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


