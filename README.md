### 使用方法
   ```bash
   https://github.com/SS-snap/ComfyUI-LBW_flux.git
   ```
克隆仓库到你的自定义节点目录中
Clone the repository into your custom node directory

### 简述
#### 通过这个节点，你可以更方便的测试关于flux_lora不同块对最终结果的影响。这是一个具有实验性的测试，因为我不能确定这58个块的由来，这是根据inspire pack中分层预设得到的结果。但在我的测试下不同块确实会对结果产生不同的影响，虽然测试结果不具备稳定性。
#### Through this node, you can more easily test the impact of different blocks in flux_lora on the final result. This is an experimental test, as I am unsure of the origin of these 58 blocks, which are derived from thelayered presets in the inspire pack. However, in my tests, different blocks do indeed have varying effects on the results, although the test results lack stability.

### 使用方法

You can use the following syntax to zero out the weights of different layers:

For example, enter 6 in layer_or_multi_layer to set the weights of layer 6 to zero.
Enter 15-30 in layer_or_multi_layer to set the weights of layers 15 to 30 to zero. Make sure to use English input and the data type should be a string.

你可以使用以下语法进行不同层权重归零
例如：
在layer_or_multi_layer中填写6，代表第6层权重为0
在layer_or_multi_layer中填写15-30，代表第15-30层权重为0
要用英文输入法输入且数据类型为字符串类型
