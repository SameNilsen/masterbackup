# AOT ID: ['0_inference']
from ctypes import c_void_p, c_long, c_int
import torch
import math
import random
import os
import tempfile
from math import inf, nan
from cmath import nanj
from torch._inductor.hooks import run_intermediate_hooks
from torch._inductor.utils import maybe_profile
from torch._inductor.codegen.memory_planning import _align as align
from torch import device, empty_strided
from torch._inductor.async_compile import AsyncCompile
from torch._inductor.select_algorithm import extern_kernels
import triton
import triton.language as tl
from torch._inductor.runtime.triton_heuristics import start_graph, end_graph
from torch._C import _cuda_getCurrentRawStream as get_raw_stream
from torch._C import _cuda_getCurrentRawStream as get_raw_stream

aten = torch.ops.aten
inductor_ops = torch.ops.inductor
_quantized = torch.ops._quantized
assert_size_stride = torch._C._dynamo.guards.assert_size_stride
assert_alignment = torch._C._dynamo.guards.assert_alignment
empty_strided_cpu = torch._C._dynamo.guards._empty_strided_cpu
empty_strided_cuda = torch._C._dynamo.guards._empty_strided_cuda
empty_strided_xpu = torch._C._dynamo.guards._empty_strided_xpu
reinterpret_tensor = torch._C._dynamo.guards._reinterpret_tensor
alloc_from_pool = torch.ops.inductor._alloc_from_pool
async_compile = AsyncCompile()
empty_strided_p2p = torch._C._distributed_c10d._SymmetricMemory.empty_strided_p2p


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/zp/czpiy2td33ydm43ccimhdlp5kqdk2xccg6haz3ydrxafsioiu34r.py
# Topologically Sorted Source Nodes: [long, embedding, to, pow_1, mean, add, rsqrt, mul, to_1, mul_1], Original ATen: [aten._to_copy, aten.embedding, aten.pow, aten.mean, aten.add, aten.rsqrt, aten.mul]
# Source node to ATen node mapping:
#   add => add_14
#   embedding => embedding
#   long => convert_element_type
#   mean => mean
#   mul => mul_10
#   mul_1 => mul_15
#   pow_1 => pow_1
#   rsqrt => rsqrt
#   to => convert_element_type_1
#   to_1 => convert_element_type_2
# Graph fragment:
#   %convert_element_type : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%arg0_1, torch.int64), kwargs = {})
#   %embedding : [num_users=2] = call_function[target=torch.ops.aten.embedding.default](args = (%arg2_1, %convert_element_type), kwargs = {})
#   %convert_element_type_1 : [num_users=2] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%embedding, torch.float32), kwargs = {})
#   %pow_1 : [num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%convert_element_type_1, 2), kwargs = {})
#   %mean : [num_users=1] = call_function[target=torch.ops.aten.mean.dim](args = (%pow_1, [-1], True), kwargs = {})
#   %add_14 : [num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%mean, 1e-05), kwargs = {})
#   %rsqrt : [num_users=1] = call_function[target=torch.ops.aten.rsqrt.default](args = (%add_14,), kwargs = {})
#   %mul_10 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%convert_element_type_1, %rsqrt), kwargs = {})
#   %convert_element_type_2 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%mul_10, torch.bfloat16), kwargs = {})
#   %mul_15 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%convert_element_type_2, %arg3_1), kwargs = {})
triton_red_fused__to_copy_add_embedding_mean_mul_pow_rsqrt_0 = async_compile.triton('triton_red_fused__to_copy_add_embedding_mean_mul_pow_rsqrt_0', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.reduction(
    size_hints={'x': 8192, 'r0_': 8192},
    reduction_hint=ReductionHint.INNER,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*i32', 'in_ptr1': '*bf16', 'in_ptr2': '*bf16', 'out_ptr0': '*bf16', 'out_ptr2': '*bf16', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr', 'R0_BLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]], (6,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_red_fused__to_copy_add_embedding_mean_mul_pow_rsqrt_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 3, 'num_reduction': 1, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False}
)
@triton.jit
def triton_red_fused__to_copy_add_embedding_mean_mul_pow_rsqrt_0(in_ptr0, in_ptr1, in_ptr2, out_ptr0, out_ptr2, xnumel, r0_numel, XBLOCK : tl.constexpr, R0_BLOCK : tl.constexpr):
    r0_numel = 5120
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_base = tl.arange(0, R0_BLOCK)[None, :]
    rbase = r0_base
    x0 = xindex
    tmp0 = tl.load(in_ptr0 + (x0), xmask, eviction_policy='evict_last')
    _tmp11 = tl.full([XBLOCK, R0_BLOCK], 0, tl.float32)
    for r0_offset in range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp1 = tmp0.to(tl.int64)
        tmp2 = tl.full([XBLOCK, R0_BLOCK], 51200, tl.int32)
        tmp3 = tmp1 + tmp2
        tmp4 = tmp1 < 0
        tmp5 = tl.where(tmp4, tmp3, tmp1)
        tl.device_assert(((0 <= tmp5) & (tmp5 < 51200)) | ~(xmask), "index out of bounds: 0 <= tmp5 < 51200")
        tmp7 = tl.load(in_ptr1 + (r0_1 + 5120*tmp5), r0_mask & xmask, eviction_policy='evict_first', other=0.0).to(tl.float32)
        tmp8 = tmp7.to(tl.float32)
        tmp9 = tmp8 * tmp8
        tmp10 = tl.broadcast_to(tmp9, [XBLOCK, R0_BLOCK])
        tmp12 = _tmp11 + tmp10
        _tmp11 = tl.where(r0_mask & xmask, tmp12, _tmp11)
        tl.store(out_ptr0 + (r0_1 + 5120*x0), tmp7, r0_mask & xmask)
    tmp11 = tl.sum(_tmp11, 1)[:, None]
    for r0_offset in range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp13 = tl.load(out_ptr0 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_first', other=0.0).to(tl.float32)
        tmp22 = tl.load(in_ptr2 + (r0_1), r0_mask, eviction_policy='evict_last', other=0.0).to(tl.float32)
        tmp14 = tmp13.to(tl.float32)
        tmp15 = 5120.0
        tmp16 = (tmp11 / tmp15)
        tmp17 = 1e-05
        tmp18 = tmp16 + tmp17
        tmp19 = libdevice.rsqrt(tmp18)
        tmp20 = tmp14 * tmp19
        tmp21 = tmp20.to(tl.float32)
        tmp23 = tmp21 * tmp22
        tl.store(out_ptr2 + (r0_1 + 5120*x0), tmp23, r0_mask & xmask)
''', device_str='cuda')


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/ur/curswfovdoq7dpf4em7lkc7h6jntqptyuq2kdasjmcomvzt56zoa.py
# Topologically Sorted Source Nodes: [cat], Original ATen: [aten.cat]
# Source node to ATen node mapping:
#   cat => cat
# Graph fragment:
#   %cat : [num_users=1] = call_function[target=torch.ops.aten.cat.default](args = ([%sub_26, %add_97], -1), kwargs = {})
triton_poi_fused_cat_1 = async_compile.triton('triton_poi_fused_cat_1', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 33554432}, 
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*bf16', 'in_ptr1': '*i64', 'in_ptr2': '*bf16', 'out_ptr0': '*bf16', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_cat_1', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 6, 'num_reduction': 0, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_cat_1(in_ptr0, in_ptr1, in_ptr2, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = tl.full([XBLOCK], True, tl.int1)
    x0 = (xindex % 128)
    x1 = ((xindex // 128) % 32)
    x2 = xindex // 4096
    x4 = xindex
    tmp0 = x0
    tmp1 = tl.full([1], 0, tl.int64)
    tmp2 = tmp0 >= tmp1
    tmp3 = tl.full([1], 64, tl.int64)
    tmp4 = tmp0 < tmp3
    tmp5 = tl.load(in_ptr0 + (128*x1 + 6144*x2 + (x0)), tmp4, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp6 = tl.load(in_ptr1 + (x2), tmp4, eviction_policy='evict_last', other=0.0)
    tmp7 = tl.full([XBLOCK], 1024000, tl.int32)
    tmp8 = tmp6 + tmp7
    tmp9 = tmp6 < 0
    tmp10 = tl.where(tmp9, tmp8, tmp6)
    tl.device_assert(((0 <= tl.broadcast_to(tmp10, [XBLOCK])) & (tl.broadcast_to(tmp10, [XBLOCK]) < 1024000)) | ~(tmp4), "index out of bounds: 0 <= tl.broadcast_to(tmp10, [XBLOCK]) < 1024000")
    tmp12 = tl.load(in_ptr2 + (128*tmp10 + (x0)), tmp4, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp13 = tmp5 * tmp12
    tmp14 = tl.load(in_ptr0 + (64 + 128*x1 + 6144*x2 + (x0)), tmp4, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp15 = tl.load(in_ptr2 + (64 + 128*tmp10 + (x0)), tmp4, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp16 = tmp14 * tmp15
    tmp17 = tmp13 - tmp16
    tmp18 = tl.full(tmp17.shape, 0.0, tmp17.dtype)
    tmp19 = tl.where(tmp4, tmp17, tmp18)
    tmp20 = tmp0 >= tmp3
    tmp21 = tl.full([1], 128, tl.int64)
    tmp22 = tmp0 < tmp21
    tmp23 = tl.load(in_ptr0 + (64 + 128*x1 + 6144*x2 + ((-64) + x0)), tmp20, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp24 = tl.load(in_ptr1 + (x2), tmp20, eviction_policy='evict_last', other=0.0)
    tmp25 = tl.full([XBLOCK], 1024000, tl.int32)
    tmp26 = tmp24 + tmp25
    tmp27 = tmp24 < 0
    tmp28 = tl.where(tmp27, tmp26, tmp24)
    tl.device_assert(((0 <= tl.broadcast_to(tmp28, [XBLOCK])) & (tl.broadcast_to(tmp28, [XBLOCK]) < 1024000)) | ~(tmp20), "index out of bounds: 0 <= tl.broadcast_to(tmp28, [XBLOCK]) < 1024000")
    tmp30 = tl.load(in_ptr2 + (128*tmp28 + ((-64) + x0)), tmp20, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp31 = tmp23 * tmp30
    tmp32 = tl.load(in_ptr0 + (128*x1 + 6144*x2 + ((-64) + x0)), tmp20, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp33 = tl.load(in_ptr2 + (64 + 128*tmp28 + ((-64) + x0)), tmp20, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp34 = tmp32 * tmp33
    tmp35 = tmp31 + tmp34
    tmp36 = tl.full(tmp35.shape, 0.0, tmp35.dtype)
    tmp37 = tl.where(tmp20, tmp35, tmp36)
    tmp38 = tl.where(tmp4, tmp19, tmp37)
    tl.store(out_ptr0 + (x4), tmp38, None)
''', device_str='cuda')


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/nn/cnnhaf5qwsy7a4vmwdehwd27zypcuyvzbw7bmm2elolcj2s5bhxa.py
# Topologically Sorted Source Nodes: [cat_2], Original ATen: [aten.cat]
# Source node to ATen node mapping:
#   cat_2 => cat_1
# Graph fragment:
#   %cat_1 : [num_users=1] = call_function[target=torch.ops.aten.cat.default](args = ([%sub_43, %add_159], -1), kwargs = {})
triton_poi_fused_cat_2 = async_compile.triton('triton_poi_fused_cat_2', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 8388608}, 
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*bf16', 'in_ptr1': '*i64', 'in_ptr2': '*bf16', 'out_ptr0': '*bf16', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_cat_2', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 6, 'num_reduction': 0, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_cat_2(in_ptr0, in_ptr1, in_ptr2, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x0 = (xindex % 128)
    x1 = ((xindex // 128) % 8)
    x2 = xindex // 1024
    x4 = xindex
    tmp0 = x0
    tmp1 = tl.full([1], 0, tl.int64)
    tmp2 = tmp0 >= tmp1
    tmp3 = tl.full([1], 64, tl.int64)
    tmp4 = tmp0 < tmp3
    tmp5 = tl.load(in_ptr0 + (4096 + 128*x1 + 6144*x2 + (x0)), tmp4 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp6 = tl.load(in_ptr1 + (x2), tmp4 & xmask, eviction_policy='evict_last', other=0.0)
    tmp7 = tl.full([XBLOCK], 1024000, tl.int32)
    tmp8 = tmp6 + tmp7
    tmp9 = tmp6 < 0
    tmp10 = tl.where(tmp9, tmp8, tmp6)
    tl.device_assert(((0 <= tl.broadcast_to(tmp10, [XBLOCK])) & (tl.broadcast_to(tmp10, [XBLOCK]) < 1024000)) | ~(tmp4 & xmask), "index out of bounds: 0 <= tl.broadcast_to(tmp10, [XBLOCK]) < 1024000")
    tmp12 = tl.load(in_ptr2 + (128*tmp10 + (x0)), tmp4 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp13 = tmp5 * tmp12
    tmp14 = tl.load(in_ptr0 + (4160 + 128*x1 + 6144*x2 + (x0)), tmp4 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp15 = tl.load(in_ptr2 + (64 + 128*tmp10 + (x0)), tmp4 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp16 = tmp14 * tmp15
    tmp17 = tmp13 - tmp16
    tmp18 = tl.full(tmp17.shape, 0.0, tmp17.dtype)
    tmp19 = tl.where(tmp4, tmp17, tmp18)
    tmp20 = tmp0 >= tmp3
    tmp21 = tl.full([1], 128, tl.int64)
    tmp22 = tmp0 < tmp21
    tmp23 = tl.load(in_ptr0 + (4160 + 128*x1 + 6144*x2 + ((-64) + x0)), tmp20 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp24 = tl.load(in_ptr1 + (x2), tmp20 & xmask, eviction_policy='evict_last', other=0.0)
    tmp25 = tl.full([XBLOCK], 1024000, tl.int32)
    tmp26 = tmp24 + tmp25
    tmp27 = tmp24 < 0
    tmp28 = tl.where(tmp27, tmp26, tmp24)
    tl.device_assert(((0 <= tl.broadcast_to(tmp28, [XBLOCK])) & (tl.broadcast_to(tmp28, [XBLOCK]) < 1024000)) | ~(tmp20 & xmask), "index out of bounds: 0 <= tl.broadcast_to(tmp28, [XBLOCK]) < 1024000")
    tmp30 = tl.load(in_ptr2 + (128*tmp28 + ((-64) + x0)), tmp20 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp31 = tmp23 * tmp30
    tmp32 = tl.load(in_ptr0 + (4096 + 128*x1 + 6144*x2 + ((-64) + x0)), tmp20 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp33 = tl.load(in_ptr2 + (64 + 128*tmp28 + ((-64) + x0)), tmp20 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp34 = tmp32 * tmp33
    tmp35 = tmp31 + tmp34
    tmp36 = tl.full(tmp35.shape, 0.0, tmp35.dtype)
    tmp37 = tl.where(tmp20, tmp35, tmp36)
    tmp38 = tl.where(tmp4, tmp19, tmp37)
    tl.store(out_ptr0 + (x4), tmp38, xmask)
''', device_str='cuda')


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/jw/cjw2jsqvss6bq5pixpu4sub2ellgiaaqtaehgzzougxyqksp5pqc.py
# Topologically Sorted Source Nodes: [view_3], Original ATen: [aten.view]
# Source node to ATen node mapping:
#   view_3 => full_default
# Graph fragment:
#   %full_default : [num_users=1] = call_function[target=torch.ops.aten.full.default](args = ([%arg1_1, 32, 128], 0.0), kwargs = {dtype: torch.bfloat16, layout: torch.strided, device: cuda:0, pin_memory: False})
triton_poi_fused_view_3 = async_compile.triton('triton_poi_fused_view_3', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 33554432}, 
    filename=__file__,
    triton_meta={'signature': {'out_ptr0': '*bf16', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_view_3', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 0, 'num_reduction': 0, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_view_3(out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = tl.full([XBLOCK], True, tl.int1)
    x0 = xindex
    tmp0 = 0.0
    tl.store(out_ptr0 + (x0), tmp0, None)
''', device_str='cuda')


async_compile.wait(globals())
del async_compile

def call(args):
    arg0_1, arg1_1, arg2_1, arg3_1, arg4_1, arg5_1, arg6_1 = args
    args.clear()
    s72 = arg1_1
    assert_size_stride(arg0_1, (s72, ), (1, ))
    assert_size_stride(arg2_1, (51200, 5120), (5120, 1))
    assert_size_stride(arg3_1, (5120, ), (1, ))
    assert_size_stride(arg4_1, (6144, 5120), (5120, 1))
    assert_size_stride(arg5_1, (s72, ), (1, ))
    assert_size_stride(arg6_1, (1024000, 128), (128, 1))
    with torch.cuda._DeviceGuard(0):
        torch.cuda.set_device(0)
        buf0 = empty_strided_cuda((s72, 5120), (5120, 1), torch.bfloat16)
        buf2 = empty_strided_cuda((s72, 5120), (5120, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [long, embedding, to, pow_1, mean, add, rsqrt, mul, to_1, mul_1], Original ATen: [aten._to_copy, aten.embedding, aten.pow, aten.mean, aten.add, aten.rsqrt, aten.mul]
        stream0 = get_raw_stream(0)
        triton_red_fused__to_copy_add_embedding_mean_mul_pow_rsqrt_0.run(arg0_1, arg2_1, arg3_1, buf0, buf2, s72, 5120, stream=stream0)
        del arg0_1
        del arg2_1
        del arg3_1
        buf3 = empty_strided_cuda((s72, 6144), (6144, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [to, pow_1, mean, add, rsqrt, mul, to_1, mul_1, linear], Original ATen: [aten._to_copy, aten.pow, aten.mean, aten.add, aten.rsqrt, aten.mul, aten.mm]
        extern_kernels.mm(buf2, reinterpret_tensor(arg4_1, (5120, 6144), (1, 5120), 0), out=buf3)
        del arg4_1
        del buf2
        buf4 = empty_strided_cuda((s72, 32, 128), (4096, 128, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [cat], Original ATen: [aten.cat]
        triton_poi_fused_cat_1_xnumel = 4096*s72
        stream0 = get_raw_stream(0)
        triton_poi_fused_cat_1.run(buf3, arg5_1, arg6_1, buf4, triton_poi_fused_cat_1_xnumel, stream=stream0)
        buf5 = empty_strided_cuda((s72, 8, 128), (1024, 128, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [cat_2], Original ATen: [aten.cat]
        triton_poi_fused_cat_2_xnumel = 1024*s72
        stream0 = get_raw_stream(0)
        triton_poi_fused_cat_2.run(buf3, arg5_1, arg6_1, buf5, triton_poi_fused_cat_2_xnumel, stream=stream0)
        del arg5_1
        del arg6_1
        buf6 = empty_strided_cuda((s72, 32, 128), (4096, 128, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [view_3], Original ATen: [aten.view]
        triton_poi_fused_view_3_xnumel = 4096*s72
        stream0 = get_raw_stream(0)
        triton_poi_fused_view_3.run(buf6, triton_poi_fused_view_3_xnumel, stream=stream0)
    return (buf4, buf5, reinterpret_tensor(buf3, (s72, 8, 128), (6144, 128, 1), 5120), buf6, buf0, )


def benchmark_compiled_module(times=10, repeat=10):
    from torch._dynamo.testing import rand_strided
    from torch._inductor.utils import print_performance
    arg0_1 = rand_strided((8192, ), (1, ), device='cuda:0', dtype=torch.int32)
    arg1_1 = 8192
    arg2_1 = rand_strided((51200, 5120), (5120, 1), device='cuda:0', dtype=torch.bfloat16)
    arg3_1 = rand_strided((5120, ), (1, ), device='cuda:0', dtype=torch.bfloat16)
    arg4_1 = rand_strided((6144, 5120), (5120, 1), device='cuda:0', dtype=torch.bfloat16)
    arg5_1 = rand_strided((8192, ), (1, ), device='cuda:0', dtype=torch.int64)
    arg6_1 = rand_strided((1024000, 128), (128, 1), device='cuda:0', dtype=torch.bfloat16)
    fn = lambda: call([arg0_1, arg1_1, arg2_1, arg3_1, arg4_1, arg5_1, arg6_1])
    return print_performance(fn, times=times, repeat=repeat)


if __name__ == "__main__":
    from torch._inductor.wrapper_benchmark import compiled_module_main
    compiled_module_main('None', benchmark_compiled_module)
