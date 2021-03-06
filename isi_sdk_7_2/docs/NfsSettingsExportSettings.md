# NfsSettingsExportSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_dirs** | **bool** | If true, all directories under the specified paths are mountable. | [optional] 
**block_size** | **int** | The block size returned by the NFS STATFS procedure. | [optional] 
**can_set_time** | **bool** | If true, the client may  set file  times using the NFS SETATTR request.  This  option is advisory and the server always behaves as if it is true. | [optional] 
**case_insensitive** | **bool** | If true, the server will report that it ignores case for file names. | [optional] 
**case_preserving** | **bool** | If true, the server will report that it always preserves case for file names. | [optional] 
**chown_restricted** | **bool** | If true, the server will report that only the superuser may change file ownership. | [optional] 
**commit_asynchronous** | **bool** | If true, allows NFS  commit  requests to  execute asynchronously. | [optional] 
**directory_transfer_size** | **int** | The preferred size for directory read operations.  This option is advisory. | [optional] 
**encoding** | **str** | The character encoding of clients connecting to the export. | [optional] 
**link_max** | **int** | The reported maximum number of links to a file. | [optional] 
**map_all** | [**NfsExportMapAll**](NfsExportMapAll.md) | User and group mapping. | [optional] 
**map_failure** | [**NfsExportMapAll**](NfsExportMapAll.md) | User and group mapping. | [optional] 
**map_full** | **bool** | If true, user mappings queries the OneFS user database.  If false, only local authentication is queried. | [optional] 
**map_lookup_uid** | **bool** | If true, incoming UIDs are mapped to users in the OneFS user database.  If false, incoming UIDs are applied directly to file operations. | [optional] 
**map_non_root** | [**NfsExportMapAll**](NfsExportMapAll.md) | User and group mapping. | [optional] 
**map_retry** | **bool** | Determines whether lookups for users specified in map_all, map_root or map_nonroot are retried if the look fails. | [optional] 
**map_root** | [**NfsExportMapAll**](NfsExportMapAll.md) | User and group mapping. | [optional] 
**max_file_size** | **int** | The maximum file size in the export. | [optional] 
**name_max_size** | **int** | The reported maximum length of a file name. | [optional] 
**no_truncate** | **bool** | If true, report that too-long file names result in an error | [optional] 
**read_only** | **bool** | If true, the export is read-only. | [optional] 
**read_transfer_max_size** | **int** | The maximum buffer size that clients should use on NFS read requests.  This option is advisory. | [optional] 
**read_transfer_multiple** | **int** | The preferred multiple size for NFS read requests.  This option is advisory. | [optional] 
**read_transfer_size** | **int** | The optimal size for NFS read requests.  This option is advisory. | [optional] 
**readdirplus** | **bool** | If true, readdirplus requests are enabled. | [optional] 
**readdirplus_prefetch** | **int** | This field is deprecated and does not do anything. | [optional] 
**return_32bit_file_ids** | **bool** | Limits the size of file identifiers returned by NFSv3+ to 32-bit values. | [optional] 
**security_flavors** | **list[str]** | The authentication flavors that are supported for this export. | [optional] 
**setattr_asynchronous** | **bool** | If true, allows setattr operations to execute asynchronously. | [optional] 
**snapshot** | **str** | Use this snapshot for all mounts. | [optional] 
**symlinks** | **bool** | If true, paths reachable by symlinks are exported. | [optional] 
**time_delta** | **float** | The resolution of all time values that are returned to clients. | [optional] 
**write_datasync_action** | **str** | The synchronization type. | [optional] 
**write_datasync_reply** | **str** | The synchronization type. | [optional] 
**write_filesync_action** | **str** | The synchronization type. | [optional] 
**write_filesync_reply** | **str** | The synchronization type. | [optional] 
**write_transfer_max_size** | **int** | The maximum buffer size that clients should use on NFS write requests.  This option is advisory. | [optional] 
**write_transfer_multiple** | **int** | The preferred multiple size for NFS write requests.  This option is advisory. | [optional] 
**write_transfer_size** | **int** | The optimal size for NFS read requests.  This option is advisory. | [optional] 
**write_unstable_action** | **str** | The synchronization type. | [optional] 
**write_unstable_reply** | **str** | The synchronization type. | [optional] 
**zone** | **str** | The zone in which the export is valid | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


