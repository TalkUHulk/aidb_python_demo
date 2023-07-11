from api import *
from .types import *
import ujson


@app.post('/aidb/register')
def register(req: RegisterReq):
    ret = AiDBRegister(g_ins, create_string_buffer(req.json().encode('utf-8')))

    reply = StatusReply(error_code=ret, msg="succeed")
    if reply.error_code != 0:
        reply.msg = "failed"

    return reply.dict()


@app.post('/aidb/unregister')
def unregister(req: UnRegisterReq):
    ret = AiDBUnRegister(g_ins, create_string_buffer(req.flow_uuid.encode('utf-8')))

    reply = StatusReply(error_code=ret, msg="succeed")
    if reply.error_code != 0:
        reply.msg = "failed"

    return reply.dict()


@app.post('/aidb/query')
def query(req: QueryReq):
    result = create_string_buffer(b"", 1024 * 1024)
    size_out = c_int(0)

    flow_uuid = create_string_buffer(req.flow_uuid.encode('utf-8'))
    images_base64 = create_string_buffer(req.image_base64.encode('utf-8'))

    ret = AiDBForward(g_ins, flow_uuid, images_base64, result, sizeof(result), pointer(size_out))

    reply = QueryReply(error_code=ret, msg="succeed")
    if reply.error_code != 0:
        reply.msg = "failed"
    else:
        aidb_output = ujson.loads(result.value.decode("utf-8"))

        for k, v in aidb_output.items():
            setattr(reply, k, v)

    return reply.dict()
