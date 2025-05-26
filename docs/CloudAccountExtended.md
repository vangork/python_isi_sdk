# CloudAccountExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | The machine generated name of the account bucket to store data | [optional] 
**id** | **str** | A globally unique name for this account | [optional] 
**metadata_bucket** | **str** | The machine generated name of the account bucket to store metadata | [optional] 
**pool** | **str** | Name of the pool referencing this account.  Empty if none. | [optional] 
**state** | **str** | Indicates whether this account is in a good state (\&quot;OK\&quot;), disabled (\&quot;disabled\&quot;) or inaccessible via the network (\&quot;unreachable\&quot;) | [optional] 
**state_details** | **str** | Gives further information to describe the state of this account | [optional] 
**type** | **str** | The type of cloud protocol required.  E.g., \&quot;isilon\&quot; for Dell EMC PowerScale, \&quot;ecs\&quot; for Dell EMC ECS Appliance, \&quot;virtustream\&quot; for Virtustream Storage Cloud, \&quot;azure\&quot; for Microsoft Azure, \&quot;s3\&quot; for Amazon S3, \&quot;c2s-s3\&quot; for Amazon Commercial Cloud Services S3 and \&quot;google\&quot; for Google Cloud Platform and \&quot;alibaba-cloud\&quot; for Alibaba Cloud | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


