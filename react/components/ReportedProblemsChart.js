import React, {useCallback} from 'react';
import { ResponsiveLine } from '@nivo/line';
import './style/chart_tooltip.scss';

const ReportedProblemsChart = ({data}) => {

    const chartsData = [
        {
            "id": "",
            "data": [
                ...data.data
            ]
        }
    ];

    const customTooltip = useCallback((value) => {
        return (
            <div className="chart_tooltip">
                <span>Date: {value.point.data.xFormatted}</span>
                <span>Count: {value.point.data.y}</span>
            </div>
        )
    }, []);

    return !!data.data.length && <div className="chart_tile problems_tile">
        <div className="chart_info_sect">
            <p>
                <span className="ws_icon"/>
                Challenges
            </p>
            <span className="secondary_title">{data.users} users</span>
            <span className='percentage_value'>{data.sum}</span>
        </div>
        <div className="chart_sect reported_problems_chart">
            <ResponsiveLine
                data={chartsData}
                lineWidth={1}
                pointSize={2}
                margin={{top: 3, right: 3, bottom: 3, left: 3}}
                yScale={{type: 'linear', min: 'auto', max: 'auto', stacked: true, reverse: false}}
                // xScale={{format: "%Y-%m-%d", type: "time"}} //todo need to get customer date format and set
                // xFormat="time:%Y-%m-%d"
                axisTop={null}
                axisRight={null}
                axisBottom={null}
                axisLeft={null}
                enableGridX={false}
                enableGridY={false}
                colors='#FF5878'
                pointColor={{ from: 'color', modifiers: [] }}
                pointBorderWidth={2}
                pointBorderColor={{ from: 'serieColor' }}
                pointLabel="y"
                pointLabelYOffset={-18}
                enableArea={true}
                areaOpacity={0.1}
                useMesh={true}
                tooltip={(value) => {
                    return customTooltip(value);
                }}
                legends={[
                    {
                        anchor: 'bottom-right',
                        direction: 'column',
                        justify: false,
                        translateX: 100,
                        translateY: 0,
                        itemsSpacing: 0,
                        itemDirection: 'left-to-right',
                        itemWidth: 80,
                        itemHeight: 20,
                        itemOpacity: 0.75,
                        symbolSize: 12,
                        symbolShape: 'circle',
                        symbolBorderColor: 'rgba(0, 0, 0, .5)',
                        effects: [
                            {
                                on: 'hover',
                                style: {
                                    itemBackground: 'rgba(0, 0, 0, .03)',
                                    itemOpacity: 1
                                }
                            }
                        ]
                    }
                ]}
            />
        </div>
    </div>
}

export default React.memo(ReportedProblemsChart);
